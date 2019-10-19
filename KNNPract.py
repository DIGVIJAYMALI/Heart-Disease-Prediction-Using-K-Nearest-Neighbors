import csv
import numpy as np
import random
import math
import operator

data = np.genfromtxt('heart_disease.csv', dtype=None, delimiter=',', skip_header=1)
print(data)
print(len(data))

def loadDataSet(data,split,trainingSet=[],testSet=[]):

    for x in range(len(data)):
        if(random.random()<split):
            trainingSet.append(data[x])
        else:
             testSet.append(data[x])

def euclidian(inst1,inst2,length):
    dist=0
    for x in range(length):
        dist+=(inst1[x]-inst2[x])**2
    return math.sqrt(dist)

def getNeighbors(train,test,k):
    distances=[]
    length=len(test)-1
    for x in range(len(train)):
        dist=euclidian(test,train[x],length)
        distances.append((train[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neigh=[]
    for x in range(k):
        neigh.append(distances[x][0])
    return neigh

def getResponse(neighbors):
    classvotes={}
    for x in range(len(neighbors)):
        response=neighbors[x][-1]
        if(response in  classvotes):
            classvotes[response]+=1
        else:
            classvotes[response]=1
        sortedvotes=sorted(classvotes.iteritems(),key=operator.itemgetter(1),reverse=True)
        return sortedvotes[0][0]

def getAccuracy(test,pred):
    correct=0
    for x in range(len(test)):
        #COMPARE LAST VALUE OF TEST WITH PRED
        if test[x][-1] is pred[x]:
            correct+=1
    return (correct/float(len(test)))*100.0

trainSet=[]
testSet=[]
loadDataSet(data,0.66,trainSet,testSet)
print("#####################train")
#print(trainSet)
print(len(trainSet))
print("#####################test")
#print(testSet)
print(len(testSet))
d1=[[2,2,2,'a'],[1,1,1,'a'],[4,4,4,'b']]
d2=[5,5,5]
k=2
neigh=getNeighbors(d1,d2,k)
print(neigh)
response=getResponse(neigh)
print(response)
#d3=euclidian(d1,d2,3)
#print(d3)