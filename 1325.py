# 효율적인해킹 => bfs로 풀것 브루트 포스 걍 bfs로 풀기
import sys

def dfs(graph, visit, node):
    global cnt
    cnt += 1
    for i in graph[node]:
        if(visit[i] is False):
            dfs(graph, visit, i)
    return cnt

N, M = list(map(int, sys.stdin.readline().strip().split()))
graph = list([] for i in range(N + 1))
count = [0] * (N + 1)

for i in range(M):
    A, B = list(map(int, sys.stdin.readline().strip().split()))
    graph[B].append(A)

for i in range(1, N+1):
    visit = [False] * (N + 1)
    cnt = 0
    count[i] = dfs(graph, visit, i)

MAX = max(count)
max_list = []
for i in range(1, N+1):
    if(MAX == count[i]):
        max_list.append(i)

for i in max_list:
    print(i, end=' ')
