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
    plt.scatter(centroids[:,0],centroids[:,1],c='black',s=100)

    distances: list = []
    for x in data:
        tmp = []
        for c in centroids:
            tmp.append(distance(x,c))
        distances.append(tmp)



    updtate_color_of_data(distances)

    plt.show()

    print(plots_by_color)


def make_centroids(k, data):
    centroids = []
    for i in range(k):
        centroids.append(data[random.randint(0,len(data)-1)])
    return np.array(centroids)

def distance(x,y):
    return np.linalg.norm(x-y)

def updtate_color_of_data(distances):
    counter = 0
    for element in distances:
        plt.scatter(data[counter][0],data[counter][1], color=find_minimnum_distance(element))
        counter = counter + 1

def find_minimnum_distance(element):
    global plots_by_color
    plots_by_color = [[], [], []]
    if element.index(min(element)) == 0:
        plots_by_color[0].append(element)
        return ['r']
    if element.index(min(element)) == 1:
        plots_by_color[1].append(element)
        return ['g']
    if element.index(min(element)) == 2:
        plots_by_color[2].append(element)
        return ['b']




if __name__ == '__main__':
    main()