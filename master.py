import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def main():
    np.random.seed(1)

    blobs = make_blobs(n_samples=50,n_features=2,centers=3)
    data = blobs[0]
    print(data)

    plt.scatter(data[:,0],data[:,1])


    K = 3
    centroids = make_centroids(K, data)
    plt.scatter(centroids[:,0],centroids[:,1],c='r',s=100,marker='x')



    plt.show()


def make_centroids(k, data):
    centroids = []
    for i in range(k):
        centroids.append(data[random.randint(0,len(data)-1)])
    return np.array(centroids)


if __name__ == '__main__':
    main()