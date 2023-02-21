import numpy as np
import sys

if sys.argv[1] == "a":
    # a. create a 20-element vector with entries from 1 to 20, and copy out all elements that are even using mask indexing!
    vec = np.arange(1, 21)
    new = vec[vec % 2 == 0] #mask indexing
    print(new)
    
if sys.argv[1] == "b":
    #    b. create a 20-element vector with entries from 1 to 20, and copy out elements
    # at positions 1, 5 amd 10 using a single operation!
    vec = np.arange(1, 21)
    new = [0, 4, 9] #mask indexing
    print(vec[new])