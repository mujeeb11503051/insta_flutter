import sys
import numpy as np

# You may need to combine Python list comprehension and numpy array creation!
if sys.argv[1] == "a":
    # a.Create a 1D array with entries from -100 to 0(included) in steps of 2
    arr = np.arange(-100, 1, 2)
    print(arr) # numpy array can be reversed using np.flip()
    
if sys.argv[1] == "b":
#  Create a 2D with 3 rows and 2 columns, with row entries 1,1..., 2,2,..., 3,3,..
    arr = np.array([1, 1, 2, 2, 3, 3])
    arr = arr.reshape([3, 2])
    print(arr)
    
if sys.argv[1] == "c":
    # Create a 2D with 3 rows and 2 columns that has the value -1 everywhere
    # ------Method 1-----
    # arr = np.full((3, 2), -1)
    
    # ------Method 2------
    
    arr = np.ones([3, 2])
    arr = arr*-1
    
    print(arr)
    
# Create a 3D tensor with shape (5,4,3) with random normal entries, with
# mean 0 and standard deviation 1.
if sys.argv[1] == "d":
    arr = np.random.normal(loc=0, scale=1, size=(5, 4, 3))
    print(arr)