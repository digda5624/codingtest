from sklearn.datasets import load_iris

import knn_class

iris = load_iris()
X = iris.data
y = iris.target
y_name = iris.target_names

# 15th data 제외 train data
X_train = X[[i - 1 for i in range(1, 151) if i % 15]]
y_train = y[[i - 1 for i in range(1, 151) if i % 15]]
# 15th data만 test
X_test = X[[i - 1 for i in range(1, 151) if i % 15 == 0]]
y_test = y[[i - 1 for i in range(1, 151) if i % 15 == 0]]

# K에 대해서 각각 다른 분류기가 생성된다(초기화)
for k in [3, 5, 10]:
    knn = knn_class.Knn_Class(k, X_train, y_train)

    print("======= 가중치를 두지 않고 계산한 knn 알고리즘 " "k =", k,  " ======= ")
    for i in range(len(X_test)):
        pred = knn.majority_vote(X_test[i])
        print("Test Data Index:", i, "/ Computed class:", y_name[pred], "/ True class:", y_name[y_test[i]], "/ Is Correct?:", y_name[pred] == y_name[y_test[i]])

    print("======= 가중치를 두고 계산한 knn 알고리즘     " "k =", k, " ======= ")
    for i in range(len(X_test)):
        pred = knn.weighted_vote(X_test[i])
        print("Test Data Index:", i, "/ Computed class:", y_name[pred], "/ True class:", y_name[y_test[i]], "/ Is Correct?:", y_name[pred] == y_name[y_test[i]])

        