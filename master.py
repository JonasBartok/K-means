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
    K = 3
    centroids = make_centroids(K, data)
    plt.scatter(centroids[:,0],centroids[:,1],c='r',s=100)

    distances: list = []
    for x in data:
        tmp = []
        for c in centroids:
            tmp.append(distance(x,c))
        distances.append(tmp)



    #find_minimnum_distance(distances)

    plt.show()


def make_centroids(k, data):
    centroids = []
    for i in range(k):
        centroids.append(data[random.randint(0,len(data)-1)])
    return np.array(centroids)

def distance(x,y):
    return np.linalg.norm(x-y)


# def find_minimnum_distance(distances):
#     index = []
#     for element in distances:
#         if element.index(min(element)) == 0:
#             plt.pcolor(data[:,0],data[:,1], color='r')
#         if element.index(min(element)) == 1:
#             plt.annotate(data[:,0],data[:,1], color='g')
#         if element.index(min(element)) == 2:
#             plt.annotate(data[:,0],data[:,1], color='b')
#             plt
        #index.append(element.index(min(element)))

    #print(index)

def updtate_color_of_data(distances):
    for element in distances:
        plt.scatter(data[:,0],data[:,1], color=find_minimnum_distance(element))

def find_minimnum_distance(distances, element):
    if element.index(min(element)) == 0:
        return ['r']
    if element.index(min(element)) == 1:
        return ['g']
    if element.index(min(element)) == 2:
        return ['b']



if __name__ == '__main__':
    main()