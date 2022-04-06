import sys
from collections import deque

def dfs(graph, node, visit):
    visit[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if(visit[i] is False):
            dfs(graph, i, visit)

def bfs(graph, node, visit):
    queue = deque([node])
    visit[node] = True

    while(queue):
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if(visit[i] is False):
                queue.append(i)
                visit[i] = True


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()

# 그래프 세팅 완료
dfs(graph, V, visit)
print()
visit = [False] * (N + 1)
bfs(graph, V, visit)