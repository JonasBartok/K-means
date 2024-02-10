import random


class KMeans:
    def __init__(self, k: int, data: list):
        # initializing some vars
        self.k: int = k
        self.data: list = data
        self._data: list = data
        self.mainlist: list = None

    def random_clusters(self) -> None:
        for _ in range(self.k):
            # inserting K number of clusters (None) into random positions
            self.data.insert(random.randint(0, len(self.data)), None)


    def get_cluster_positions(self) -> None:
        # making a dict with the positions of the clusters for later use
        self.cluster_positions: list = []
        # counter for the cluster's position
        self.clusters_position_counter: int = 0
        self.cluster_name_counter: int = 0

        for i in self.data:
            if i == None:
                # assigning values to dict --example: {1: 0, 2: 6, 3: 10}
                self.cluster_positions.append(self.clusters_position_counter)
            self.clusters_position_counter += 1

            self._cluster_positions = self.cluster_positions



    def calculate_distance(self):
        if self.mainlist == None:
            self.mainlist: list = []


            for p in range(len(self.data)):
                self.mainlist.append([])


            self.x = None
            for x in range(len(self.data)):
                for m in range(len(self.cluster_positions)):
                    self.mainlist[x].append(abs(self.cluster_positions[m] - x))

            counter = 0
            for h in range(2):
                counter = 0
                for lists in self.mainlist:
                    if 0 in lists:
                        self.mainlist.pop(counter)
                    counter = counter + 1
        else:
            self.mainlist: list = []
            for l in range(len(self.data)):
                self.mainlist.append([])

            self.a = None
            for x in range(len(self.data)):
                for m in range(len(self._cluster_positions)):
                    self.mainlist[x].append(abs(self.cluster_positions[m] - x))

            counter = 0
            for h in range(2):
                counter = 0
                for lists in self.mainlist:
                    if 0 in lists:
                        self.mainlist.pop(counter)
                    counter = counter + 1

        #print(f"The main list: {self.mainlist}")


    def find_smallest_number_in_lists(self):
        self.smallest_number: float = 0
        self.smallest_number_index: float = 0
        self.smallest_number_list: list = []

        global mainlist2
        self.mainlist2: list = []
        for p in range(len(self._cluster_positions)):
            self.mainlist2.append([])


        for lists in self.mainlist:
            self.smallest_number = float(min(lists))
            self.smallest_number_index = lists.index(self.smallest_number)

            self.mainlist2[self.smallest_number_index].append(self.smallest_number)

        #print(f"mainlist2: {self.mainlist2}")



    def calculate_mean(self):
        average: list = []

        for lists in self.mainlist2:
            try:
                average.append(float(sum(lists) / len(lists)))
            except ZeroDivisionError:
                average.append(0)

        if average == self.cluster_positions:
            print("The average is equal to the cluster positions")
            print(f"average: {average}")
            print(f"average: {sum(average) / len(average)}")
            print(f"mainlist: {self.mainlist2}")
            exit()

        self.average: list = average

        self.cluster_positions = average

        #print(f"average: {self.cluster_positions}")

    def exit_with_error(self):
        print(f"average: {self.average}")
        print(f"average: {sum(self.average) / len(self.average)}")
        print(f"mainlist: {self.mainlist2}")
        exit()

def main():
    clusters = int(input("Enter the number of clusters: "))
    data = input("Enter the data: ").split()
    k = KMeans(k=clusters,
               data=data)
    k.random_clusters()
    k.get_cluster_positions()
    for _ in range(10000):
        k.calculate_distance()
        k.find_smallest_number_in_lists()
        k.calculate_mean()
    k.exit_with_error()


if __name__ == "__main__":
    main()





