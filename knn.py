import numpy as np
from collections import Counter


class KNN:
    def __init__(self, k, distance_function):
        """
        :param k: int
        :param distance_function
        """
        self.k = k
        self.distance_function = distance_function

    # TODO: save features and lable to self
    def train(self, features, labels):
        """
        In this function, features is simply training data which is a 2D list with float values.
        For example, if the data looks like the following: Student 1 with features age 25, grade 3.8 and labeled as 0,
        Student 2 with features age 22, grade 3.0 and labeled as 1, then the feature data would be
        [ [25.0, 3.8], [22.0,3.0] ] and the corresponding label would be [0,1]

        For KNN, the training process is just loading of training data. Thus, all you need to do in this function
        is create some local variable in KNN class to store this data so you can use the data in later process.
        :param features: List[List[float]]
        :param labels: List[int]
        """
        self.features=features
        self.labels=labels
        # print(len(features), len(features[0]))
        # print(features)
        # print(len(labels))
        # print(labels)


    # TODO: predict labels of a list of points
    def predict(self, features):
        """
        This function takes 2D list of test data points, similar to those from train function. Here, you need process
        every test data point, reuse the get_k_neighbours function to find the nearest k neighbours for each test
        data point, find the majority of labels for these neighbours as the predict label for that testing data point.
        Thus, you will get N predicted label for N test data point.
        This function need to return a list of predicted labels for all test data points.
        :param features: List[List[float]]
        :return: List[int]
        """
        maxPredlabel=[]
        kindicesfor1F=[]
        count1C=0
        count2C=0
        for i in features:
            kindicesfor1F=self.get_k_neighbors(i)
            for j in kindicesfor1F:
                if j==1:
                    count1C +=1
                else:
                    count2C +=1
            if(count1C>=count2C):
                maxPredlabel.append(1)
            else:
                maxPredlabel.append(0)
            count1C=0
            count2C=0
        return maxPredlabel

    # TODO: find KNN of one point
    def get_k_neighbors(self, point):
        """
        This function takes one single data point and finds k-nearest neighbours in the training set.
        You already have your k value, distance function and you just stored all training data in KNN class with the
        train function. This function needs to return a list of labels of all k neighours.
        :param point: List[float]
        :return:  List[int]
        """
        totaldist=[]
        kindexes=[]
        countc1=0
        countc2=0
        for i in self.features:
            totaldist.append(self.distance_function(i,point))
        for i in range(self.k):
            minindex= totaldist.index(min(totaldist))

            totaldist[minindex]=np.inf
            kindexes.append(self.labels[minindex])
        return kindexes




if __name__ == '__main__':
    print(np.__version__)
