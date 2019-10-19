import numpy as np
import utils

def Calc(features):
    A=features
    features= np.array(features)
    print(features[:, 1])
    normFeat = []
    newInvFeat = []
    m = len(features)
    n = len(features[0]) if m else 0
    minA = [0 for x in range(n)]
    maxA = [0 for x in range(n)]
    print(minA)
    print("!!!!!!!!!!!!!")
    print(maxA)
    for i in range(n):
        minA[i] = min(features[:,i])
        maxA[i] = max(features[:,i])

    for i in A:
        x=0
        for j in i:
            newInvFeat.append((j - minA[x]) / (maxA[x] - minA[x]))
            x+=1
        normFeat.append(newInvFeat)
        newInvFeat = []


    return normFeat



#[[1, 0], [0, 1], [0.333333, 0.16667]]
# print(Calc( [[2, -1], [-1, 5], [0, 0]]))

train_features = [[0, 10], [2, 0]]
test_features = [[20, 1]]

scaler1 = utils.MinMaxScaler()
train_features_scaled = scaler1(train_features)
print(train_features_scaled)
# train_features_scaled should be equal to [[0, 1], [1, 0]]

test_features_scaled = scaler1(test_features)
print(test_features_scaled)
# test_features_scaled should be equal to [[10, 0.1]]

new_scaler = utils.MinMaxScaler() # creating a new scaler
_ = new_scaler([[1, 1], [0, 0]]) # new trainfeatures
test_features_scaled = new_scaler(test_features)
print(test_features_scaled)
# now test_features_scaled should be [[20, 1]]
