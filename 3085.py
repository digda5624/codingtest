import sys
N = int(input())
data = []
colorList = ['C', 'P', 'Z', 'Y']
count = 0

data.append(list(['0']*(N+2)))
for _ in range(N):
    a = list('0' + sys.stdin.readline().rstrip() + '0')
    data.append(a)
data.append(list(['0']*(N+2)))
print(data)

# 한행 한 열 씩 돌아보면서 가장 긴거 체킹 하겠지?
# for color in colorList:
#     for i in range(N):
#         for j in range(N):
# 한번에 짤 생각 하지말고 천천히 생각해보자
