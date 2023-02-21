# Before starting, create the 3D array td that is supposed to be a stack of 50
# (mono) images of size 5×5. An image at index i should have entries i everywhere.
# Give code snippets for the following operations:

import numpy as np
import sys

td = np.stack([np.full((5, 5), i) for i in range(50)])
# print("shape", td)

# ----------Similar to 
# td = []
# for i in range(50):
#     td.append(np.full((5, 5), i))
# td = np.stack(td)

if sys.argv[1] == "a":
    # a. Slice out the 1st sample into an array x and print it!
    print(td[0])
    
if sys.argv[1] == "b":
    # b. Set the 2 lowermost columns of the 10th to -1
    td[9, :, 3:] = -1
    print(td[9])
    
if sys.argv[1] == "c":
    # c. Print the mean pixel value in the 10th data sample
    new_data = td[9, :, :]
    mn = np.mean(new_data)
    #print (new_data)
    print(mn)
    
if sys.argv[1] == "d":
#d) Generate the following variations of the 10th sample and store them in a
# new variable z:
# - just keep every 3rd row
# - just keep every 3rd column
# - inverse all rows but not columns
# - invert rows but not colums, just keeping every 2th row
    # first_ans = td[9, 2, :]
    td[9] = np.stack([np.full((5), i) for i in range(1, 6)]) #just to make sure our answer is correct
    # print(td[9, 2, :]) #1
    # print(td[9, :, 3]) #2
    # td[9, ::-1, :] = td[9, :, :] #3
    # td[9, ::-2, ::] = td[9, :, :][::2] #4
    
    print(td[9, :, :][::2])
    
if sys.argv[1] == "e":
    # Apply the in-place transform 1 + x to all samples.
    td += 1
    print(td)