import sys
N = int(input())
graph = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N))

#R G B 순으로 min 값 저장
cost = list([0] * 3 for _ in range(N))
cost[0][0] = graph[0][0]
cost[0][1] = graph[0][1]
cost[0][2] = graph[0][2]

for i in range(1, N):
    cost[i][0] = min(cost[i - 1][1] + graph[i][0], cost[i - 1][2] + graph[i][0])
    cost[i][1] = min(cost[i - 1][0] + graph[i][1], cost[i - 1][2] + graph[i][1])
    cost[i][2] = min(cost[i - 1][0] + graph[i][2], cost[i - 1][1] + graph[i][2])

print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))