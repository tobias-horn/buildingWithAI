import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest_index = -1
    min_distance = np.inf  # Use np.inf as the initial minimum distance for a more generic approach

    for index, value in enumerate(x_train):
        distance = dist(value, x_test)  # Calculate distance once
        # print(distance)  # Optional: for debugging
        
        if distance < min_distance:
            min_distance = distance  # Update the minimum distance
            nearest_index = index

    # After finding the nearest vector
    print(nearest_index)
    return nearest_index  # Optionally return the index of the nearest neighbor

nearest(x_train, x_test)
