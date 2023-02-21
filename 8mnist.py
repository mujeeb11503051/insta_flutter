import numpy as np
import requests
import os
import sys
import matplotlib.pyplot as plt



if __name__ == "__main__":

  ## download MNIST if not present in current dir!
  if os.path.exists("./mnist.npz") == False:
    print ("Downloading MNIST...")
    fname = 'mnist.npz'
    url = 'http://www.gepperth.net/alexander/downloads/'
    r = requests.get(url+fname)
    open(fname , 'wb').write(r.content)
  
  ## read it into 'traind' and 'trainl'
  data = np.load("mnist.npz")
  traind = data["arr_0"]
  trainl = data["arr_2"]
  
  if sys.argv[1] == "a":
    #a) Display samples nr. 5,6 and 7 in a single figure
    #   one = traind[5, :, :] # image of picture 2
    #   two = traind[6, :, :]# image of picture 1
    #   three = traind[7, :, :]# image of picture 3
    #   samples = np.stack([one, two, three])
    #   plt.plot(one, two, three)
    #   plt.show()
    #   samples = traind[5:8]
    #   print(stack.shape)

# Create a figure with 3 subplots (1 row, 3 columns)
      fig, axs = plt.subplots(1, 3)

# Plot each sample in a separate subplot
      axs[0].imshow(traind[5])
      axs[1].imshow(traind[6])
      axs[2].imshow(traind[7])

# Remove the axis labels and add a title
    #   for ax in axs:
    #       ax.axis('off')
      fig.suptitle("Samples 5, 6 and 7")

# Show the figure
      plt.show()
      pass

  if sys.argv[1] == "b":
    #Compute the mean pixel value for each image and display all means in a
    # scatter plot!
    # mean = np.stack([np.mean(i) for i in traind])
    mean = np.stack([np.mean(traind[i]) for i in range(60000)])
    print(mean)
    plt.scatter(np.arange(60000), mean)
    # plt.scatter(range(len(mean)), mean)
    plt.show()
    pass

  if sys.argv[1] == "c":
    #Copy out all the images whose mean pixel value is > 0.3 and display 3 of them
    
    mean_data = np.mean(traind, axis=(1, 2))
    # mean_data = np.stack([np.mean(traind[i]) for i in range(len(traind))])
    
    mean_data_with_condition = traind[mean_data > .3]
    
    # print(np.mean(traind, axis=(1, 2)).shape)
    
    fig, ax = plt.subplots(1, 3)
    ax[0].imshow(traind[1])
    ax[1].imshow(traind[2])
    ax[2].imshow(traind[3])
    plt.show()
   
    pass

  if sys.argv[1] == "d":
    #   Compute the “variance image” over all samples and display it! 
    vari = np.var(traind, axis=1)
    plt.imshow(vari)
    plt.show()
    pass

  if sys.argv[1] == "e":
    # e) Copy out 10 random images and display them in a single figure!
    rand = np.stack([np.random.randint(1, len(traind)) for i in range(10)])
    
    fig, ax = plt.subplots(1, 10)
    
    for i in range(10):
        ax[i].imshow(traind[rand[i]])
    
    plt.show()
    
    pass

  if sys.argv[1] == "f":
    #   Copy out all samples of class 5 and display 10 of them!
    # new = traind[trainl == 5]
    # print(trainl.shape)
    # plt.imshow(trainl[1])
    class5 = np.where(trainl[:, 5] == 1)[0]
    
    data = traind[class5]
    
    fig, ax = plt.subplots(1, 10)
    
    for i in range(10):
        ax[i].imshow(data[i])
        ax[i].imshow(data[i])
    
    
    print(data.shape)
    
    plt.show()
    
    pass