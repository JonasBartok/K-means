import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

def main():
    global data
    np.random.seed(1)

    #create data
    blobs = make_blobs(n_samples=50, n_features=2, centers=3)
    data = blobs[0]

    plt.scatter(data[:,0],data[:,1])

    #creat centroids
    K = ask_for_number_of_clusters()
    centroids = make_centroids(K, data)


    while True:
        ordered_data: list = []
        for x in data:
            tmp = []
            for c in centroids:
                ordered_data.append([])
                tmp.append(distance(x, c))
            minimum = tmp.index(min(tmp))
            for j in range(len(centroids)):
                if minimum == j:
                    ordered_data[j].append(x)

        ordered_data = [np.array(cluster) for cluster in ordered_data if np.array(cluster).any()]



        mean = [[] for _ in range(K)]
        for z in range(len(ordered_data)):
            mean[z] = (ordered_data[z].mean(axis=0))

        mean = np.array(mean).tolist()
        centroids = np.array(centroids).tolist()

        if mean == centroids:
            break

        centroids = mean

    for b in ordered_data:
        plt.scatter(b[:, 0], b[:, 1])
        plt.scatter(np.array(centroids)[:, 0], np.array(centroids)[:, 1], color='black')

    plt.show()

def make_centroids(k, data):
    centroids = []
    for i in range(k):
        centroids.append(data[random.randint(0,len(data)-1)])
    return np.array(centroids)

def distance(x,y):
    return np.linalg.norm(x-y)

def ask_for_number_of_clusters():
    return int(input("Enter number of clusters: "))



if __name__ == '__main__':
    main()