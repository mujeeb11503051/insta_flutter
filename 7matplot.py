import sys
import numpy as np
import matplotlib.pyplot as plt

# plot the function 1/x between 1 and 5 using 100 support points!
if sys.argv[1] == "a":
    x = np.linspace(1, 5, 100)
    y = 1/x
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("The figure is:")
    plt.show()
   
# generate a scatter plot of the same data as in a)! 
if sys.argv[1] == "b":
    x = np.linspace(1, 5, 100)
    y = 1/x
    plt.scatter(x, y)
    plt.show()
# generate a scatter plot of the same data as in a)! 
if sys.argv[1] == "d":
    x = np.linspace(1, 5, 100)
    y = 1/x
    z = x ** .5 #np.sqrt(x)
    plt.plot(x, y)
    plt.plot(x, z)
    plt.show()
    
#  generate 100 numbers distributed according to a uniform distribution between 0 and 1, and display their histogram!
if sys.argv[1] == "e":
    x = np.linspace(0, 1, 100)
    plt.hist(x)
    plt.show()