import numpy as np
import math

text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

def distance(row1, row2):
    row1 = np.asarray(row1); row2 = np.asarray(row2)
    difference = sum(abs(row1 - row2))
    return difference

def main(text):

    docs = [line.split() for line in text.splitlines()] # split text into lines and lists of words
    N = len(docs)
    vocabulary = list(set(text.split())) # create the vocabulary: the list of words that appear at least once

    df = {}; tf = {}
    for word in vocabulary:
        tf[word] = [doc.count(word)/len(doc) for doc in docs]
        df[word] = sum([word in doc for doc in docs])/N
    
    full_tfidf = []
    for doc_index, doc in enumerate(docs):
        tfidf = []
        for word in vocabulary:
            tf_idf_val = tf[word][doc_index]*math.log(1/df[word],10)
            tfidf.append(tf_idf_val) 
        full_tfidf.append(tfidf)
    dist = [[distance(sent1, sent2) for sent1 in full_tfidf] for sent2 in full_tfidf]
    all_of_them = np.asarray(dist).astype('float')
    all_of_them[all_of_them==0] = np.nan
    print(np.unravel_index(np.nanargmin(all_of_them), all_of_them.shape))
        
main(text)