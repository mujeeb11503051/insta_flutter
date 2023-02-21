import sys
import numpy as np

td = np.stack([np.full((5, 5), i) for i in range(50)])
# a)  Using ‘td’... create a 5-element row vector with entries from 1 to 5, and subtract it from
# all rows of all samples using broadcasting
if sys.argv[1] == "a":
    five_el_vec = np.arange(1, 6)
    res = td - five_el_vec
    print(res)

#b) create a 5-element column vector with entries from 1 to 5, and multiply it
# with all columns of all samples using broadcasting
if sys.argv[1] == "b":
    five_el_vec = np.arange(1, 6).reshape((5, 1))
    res = td * five_el_vec
    print(res)
    
#c)  compute the mean image over all samples, and subtract it from all samples
# via broadcasting
if sys.argv[1] == "c":
    res = td - np.mean(td, axis=0)
    print(res)