import sys
import numpy as np

td = np.stack([np.full((5, 5), i) for i in range(50)])

# Take the array ‘td’ from the previous exercise and ..
if sys.argv[1] == "a":
    # a. Compute the pixel variance for pixel 0,0 over all samples
    px_var = np.var(td[:, 0, 0])
    print(px_var)
    
if sys.argv[1] == "b":
    # b.  Compute the pixel argmax for pixel 0,0 over all samples
    px_argm = np.argmax(td[:, 0, 0])
    print(px_argm) #This means that the maximum value at pixel (0, 0) over all samples is at the 50th image (index 49), which has a value of 49.
    
if sys.argv[1] == "c":
    # c.  Compute the “standard deviation image” over all samples
    st_d = np.std(td, axis=0)
    print(st_d)
    
if sys.argv[1] == "d":
    # d.  Compute the row-wise mean over all samples
    row_mean = np.mean(td, axis=2)
    print(row_mean)
    
    
if sys.argv[1] == "e":
    # e. Compute the column-wise mean over all samples
    row_col = np.mean(td, axis=1)
    print(row_col)
    
    