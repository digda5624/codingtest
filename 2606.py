#2606번
import sys
from collections import deque

def bfs(graph, start, visit):
    visit[start] = True
    queue = deque([start])
    count = 0

    while(queue):
        node = queue.popleft()
        for i in graph[node]:
            if(visit[i] == False):
                visit[i] = True
                queue.append(i)
                count += 1
    return count

def dfs(graph, node, visit):
    visit[node] = True
    global count
    for i in graph[node]:
        if(visit[i] is False):
            count += 1
            dfs(graph, i, visit)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
count = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(graph, 1, visit)
print(count)
