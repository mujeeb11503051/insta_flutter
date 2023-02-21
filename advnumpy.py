import sys
import numpy as np

# a> Give a code snippet that create two random 1D arrays of length 20, with
# integer entries between 0 and 3 (included). Then, the code should compute the
# confusion matrix from these two vectors.
if sys.argv[1] == "a":
    first1D = np.random.randint(0 , 3, 20)
    second2D = np.random.randint(0 , 3, 20)
    # Compute the confusion matrix
    cm = np.zeros((3,3), dtype=int)
    for i in range(20):
        cm[first1D[i], second2D[i]] += 1

    print(first1D)
    print(second2D)
    print(cm)

# b> Give a code snippet that generates two 1D arrays with values from 0 to 19
# (included) in ascending order. Then, the code should shuffle both arrays such
# that same positions contain same values after shuffling (like you would shuffle
# train data and labels).
if sys.argv[1] == "b":
    # Generate two 1D arrays with values from 0 to 19
    arr1 = np.arange(0, 20)
    arr2 = np.arange(20, 40)
    
    # Shuffle both arrays such that same positions contain same values
    perm = np.random.permutation(20)
    # Shuffle both arrays using the permutation
    arr1 = arr1[perm]
    arr2 = arr2[perm]

    print(arr1)
    print(arr2)
    
# c> Give a code snippet that creates a 1D array with random values from 0 to
# 9 (included). Then, interpret this array as scalar targets and create a one-hot
# representation for them, assuming 10 classes.
if sys.argv[1] == "c":
    rand_val = np.random.randint(0, 10, 10)
    one_hot = np.zeros((10, 10))
    one_hot[np.arange(10), rand_val] = 1

    print(rand_val)
    print(one_hot)