#다익스트라 알고리즘 으로 풀어보자
# 비용이 0 일때 또한 신경 써주어야 한다.
import sys

def cheapest(cost, visit):
    global N
    index = 0
    m = int(1e9)
    for i in range(1, N+1):
        if(visit[i] is False):
            if(m > cost[i]):
                m = cost[i]
                index = i
            # if문 사용안하고 min(m, cost[i]) 로 했을 경우에
            # return m
    return index

def da(graph, cost, visit):
    for _ in range(N):
        index = cheapest(cost, visit)
        # index = cost.index[m] 으로 했을 때 비용이 0인 경우에는 오류가 발생하게된다.
        if(index == 0 or visit[a] is True):
            return
        visit[index] = True
        for (i, j) in graph[index]:
            cost[i] = min(cost[i], cost[index] + j)

N = int(input())
graph = [[] for _ in range(N+1)]
cost = [int(1e9)] * (N+1)
visit = [False] * (N+1)
M = int(input())
for i in range(M):
    s, a, c = map(int, sys.stdin.readline().rstrip().split())
    graph[s].append((a, c))

s, a = map(int, sys.stdin.readline().split())
cost[s] = 0
da(graph, cost, visit)
print(cost[a])



