from sklearn.neighbors import KNeighborsClassifier
import numpy as np

class Knn_Class():
    #X 는 분류기에 넣어줄 데이터 값 y는 각각 분류기가 의미하는 아이리스 종류 knn에서 사용될 distance
    def __init__(self, K, X, y):
        # 이 부분에서 학습해야할지 잘 모르겠음
        self.X = X
        self.y = y
        self.K = K

    
    # Obtain K-Nearest Neighbor
    # 일정 거리 안에 있는 이웃들을 찾는 함수 obtain_knn
    def obtain_knn(self, test_Data):
        knn = []
        for i, x in enumerate(self.X):
            distance = self.distance(test_Data, x)
            if (distance < self.K):
                # 거리가 K 보다 작은 index 저장 이웃 추가
                knn.append((i, distance))
        # knn 을 반환
        return knn

    
    # weighted majority vote
    # obtain_knn 을 사용해 가져온 knn들을 거리에 따라 가중치를 부여하여 확률 적으로 표현하기 위해 count list에 담는다
    def weighted_vote(self, test_Data):
        knn = self.obtain_knn(test_Data)
        count = [0] * 3
        for index, distance in knn:
            count[self.y[index]] += 1 / (distance + 1)
        #count list 중에서 가장 큰 값이 확률적으로 높으므로 해당 값을 반환한다.
        return np.argmax(count)
        # 가중치에 따라 계산

    # Obtain majority vote
    # obtain_knn 을 사용해 가져온 knn들이 몇개 존재하는지 표현하기 위해 count list에 담는다
    def majority_vote(self, test_Data):
        knn = self.obtain_knn(test_Data)
        count = [0] * 3
        for index, distance in knn:
            count[self.y[index]] += 1
        #가장 knn이 많은 품종의 index를 반환한다.
        return np.argmax(count)

    # 거리 계산 하는 함수 점 A와 B 계산 유클리드 사용
    def distance(self, A, B):
        sum = 0
        for i in range(len(A)):
            sum += (A[i] - B[i]) ** 2
        return np.sqrt(sum)


