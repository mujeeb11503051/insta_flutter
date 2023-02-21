import numpy as np
import requests
import os
import sys
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # download MNIST if not present in current dir!
    if os.path.exists("./mnist.npz") == False:
        print("Downloading MNIST...")
        fname = 'mnist.npz'
        url = 'http://www.gepperth.net/alexander/downloads/'
        r = requests.get(url+fname)
        open(fname, 'wb').write(r.content)

    # read it into 'traind' and 'trainl'
    data = np.load("mnist.npz")
    traind = data["arr_0"]
    trainl = data["arr_2"]
    traind = traind.reshape(60000, 784)

    if sys.argv[1] == "1":

        ex1_1 = [i for i in range(10, 21) if i % 2 == 1]
        print(ex1_1)

        ex1_2 = [i for i in range(100, -1, -1) if i % 10 == 0]
        print(ex1_2)

        ex1_3 = [i for i in range(15, 0, -1) if i % 3 == 0]
        print(ex1_3)

        ex1_4 = ['x'*i for i in range(1, 11)]
        print(ex1_4)

        ex1_5 = ['string'+str(i) for i in range(5, 0, -1)]
        print(ex1_5)

        ex1_6 = ['1', 1, 1.0, 'one']
        print(ex1_6)

        ex1_7 = [i for i in range(0, 100) if str(i).find('5') != -1]
        print(ex1_7)

    if sys.argv[1] == "2":
        ex2_1 = np.arange(-100, 1, 2)
        ex2_1 = np.linspace(-100, 0, 51, dtype=int)
        print(ex2_1)

        ex2_2 = np.array([[i, i, i, i] for i in range(1, 5)])
        print(ex2_2)

        ex2_3 = np.ones([3, 2]).astype(int) * -1
        ex2_3 = np.zeros([3, 2]).astype(int) - 1
        print(ex2_3)

        ex2_4 = np.random.normal(0, 1, size=[5, 4, 3])
        print(ex2_4)

    if sys.argv[1] == "3":
        td = np.ones([50, 5, 5]) * np.arange(0, 50, 1).reshape(50, 1, 1)

# =============================================================================
#     td1 = np.ones([50,5,5]).astype(int)
#     for i in range(50):
#         td1[i] = td1[i]*i
# =============================================================================
        ex3_1 = td[0]

        # Ex3_2
        td[9, -2:, :] = -1
        print(td[9])

        # Ex3_3
        print(td[9].mean())

        # Ex3_4
        z = td[9]

        z1 = z[::3, ::]
        print(z1)

        z2 = z[::, ::3]
        print(z2)

        z3 = z[::-1, ::]
        print(z3)

        z4 = z[::-2, ::]
        print(z4)

        # Ex3_5
        z += 1
        print(z)

    if sys.argv[1] == "4":
        td = np.ones([50, 5, 5]) * np.arange(0, 50, 1).reshape(50, 1, 1)

        ex4_1 = np.var(td[:, 0, 0], axis=0)
        print(ex4_1)

        ex4_2 = np.argmax(td[:, 0, 0], axis=0)
        print(ex4_2)

        ex4_3 = np.std(td, axis=0)
        print(ex4_3)

        ex4_4 = np.mean(td, axis=1)
        print(ex4_4.shape)

        ex4_5 = np.mean(td, axis=2)
        print(ex4_5.shape)

    if sys.argv[1] == "5":
        td = np.ones([50, 5, 5]) * np.arange(0, 50, 1).reshape(50, 1, 1)

        newVec = np.arange(1, 6).reshape(1, 1, 5)
        print(newVec)
# =============================================================================
#       print(newVec.reshape(1, 1, 5))
#       print(newVec.reshape(1, 5, 1))
# =============================================================================
        ex5_1 = td - newVec
        print(ex5_1[0])

        ex5_2 = td * newVec.reshape(1, 5, 1)
        print(ex5_2[1])

        ex5_3 = td - np.mean(td, axis=0).reshape(1, 5, 5)
        print(ex5_3[1])

    if sys.argv[1] == "6":
        x = np.arange(0, 21)
        print('x: ', x)
# =============================================================================
#       ex6_1 = (x%2==0)
#       print(x[ex6_1])
# =============================================================================

        print(x[(x % 2 == 0)])

        x = np.arange(0, 21)
        print(x[[1, 5, 10]])
# =============================================================================
#       ex6_2 = [1, 5, 10]
#       ex6_2 = x[ex6_2]
#       print(ex6_2)
# =============================================================================

    if sys.argv[1] == "7a":
        x = np.linspace(1, 5, 100)
        plt.plot(x, 1/x)
        plt.show()

    if sys.argv[1] == "7b":
        # B
        x = np.linspace(1, 5, 100)
        plt.scatter(x, 1/x)
        plt.show()

    if sys.argv[1] == "7c":
        # B
        x = np.linspace(1, 5, 100)
        plt.bar(x, 1/x)
        plt.show()

    if sys.argv[1] == "7d":
        # B
        x = np.linspace(1, 5, 100)
        plt.plot(x, 1/x)
        plt.plot(x, np.sqrt(x))
        plt.show()

    if sys.argv[1] == "7e":
        x = np.random.uniform(0, 1, size=100)
        plt.hist(x)
        plt.show()

    if sys.argv[1] == "8a":
        print(traind.shape)
        traind = traind.reshape(-1, 28, 28)
        print(traind.shape)

        f = plt.figure()

        f.add_subplot(1, 3, 1)
        plt.imshow(traind[4])

        f.add_subplot(1, 3, 2)
        plt.imshow(traind[5])

        f.add_subplot(1, 3, 3)
        plt.imshow(traind[6])

        plt.show()

    if sys.argv[1] == "8b":
        print(traind.shape)
        mean = np.mean(traind, axis=1)
        print(mean.shape)
        plt.scatter(range(0, mean.shape[0]), mean)
        plt.show()

    if sys.argv[1] == "8c":
        meanMask = np.mean(traind, axis=1) > 0.3
        img = traind[meanMask].reshape(-1, 28, 28)

        f = plt.figure()

        f.add_subplot(1, 3, 1)
        plt.imshow(img[4])

        f.add_subplot(1, 3, 2)
        plt.imshow(img[5])

        f.add_subplot(1, 3, 3)
        plt.imshow(img[6])

        plt.show()

    if sys.argv[1] == "8d":
        variance = np.var(traind, axis=0).reshape(28, 28)
        plt.imshow(variance)
        plt.show()

    if sys.argv[1] == "8e":
        random_index = np.random.randint(0, traind.shape[0], 10)
        img = traind[random_index].reshape(-1, 28, 28)

        f = plt.figure()
        for i in range(0, 10):
            f.add_subplot(2, 5, i+1)
            plt.imshow(img[i])
        plt.show()

    if sys.argv[1] == "8f":
        print(trainl[:10])
        mask = (trainl.argmax(axis=1) == 5)
        img = traind[mask].reshape(-1, 28, 28)

        f = plt.figure()
        for i in range(0, 10):
            f.add_subplot(2, 5, i+1)
            plt.imshow(img[i])
        plt.show()

    if sys.argv[1] == "11":
        import tensorflow as tf

        def softmax(x):
            e = tf.math.exp(x)
            rowWiseSum = tf.reduce_sum(e, axis=1, keepdims=True)
            return e/rowWiseSum

        x1 = tf.constant([[-1., -1, 5], [1., 1, 2]])
        x2 = tf.constant([[1., 1, 2]])

        print(softmax(x1), softmax(x2))

    if sys.argv[1] == "12":
        import tensorflow as tf

        def MSE(Y, T):
            tmp = (Y-T)**2.
            return tf.reduce_sum(tmp) / Y.shape[0]

        T = tf.constant([[0, 0, 1.] for i in range(0, 3)])
        Y = tf.constant([[0.1, 0.1, 0.8], [0.3, 0.3, 0.4], [0.8, 0.1, 0.1]])
        print(MSE(Y, T))
        print(MSE(Y[0:2], T[0:2]))

    if sys.argv[1] == "20":
        import tensorflow as tf

        # we assume x is 1D TF tensor
        def f(x):
            # create 1D vector that counts up from 1
            tmp = tf.range(1.0, x.shape[0] + 1)
            return tf.reduce_sum(x * tmp)

        a1 = tf.constant([1., 5, 3])  # decimal point to have float dtype
        a2 = tf.constant([2., 0, 2])  # for a1 and a2
        print("20a", f(a1), f(a2))

        # persistent = True if g is used for several gradient computations, not just one
        with tf.GradientTape(persistent=True) as g:
            # need to watch both constants, otherwise grad w.r.t. both will be None
            g.watch(a1)
            # This is because by default, TF watches only tf.Variables
            g.watch(a2)
            y1 = f(a1)
            y2 = f(a2)

        print("20b", g.gradient(y1, a1))
        # TF always computes whole gradient, from which we extract entry nr. 1
        print("20c", g.gradient(y2, a2)[0])