import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def distance(row1, row2):
    row1 = np.asarray(row1); row2 = np.asarray(row2)
    difference = sum(abs(row1 - row2))
    return difference

def all_pairs(data):
    dist = [[distance(sent1, sent2) for sent1 in data] for sent2 in data]
    return dist

def find_nearest_pair(data):
    all_of_them = np.asarray(all_pairs(data)).astype('float')
    all_of_them[all_of_them==0] = np.nan
    print(np.unravel_index(np.nanargmin(all_of_them), all_of_them.shape))

find_nearest_pair(data)