#트리 문제 dfs로 해결함

import sys

def rmNode(graph, node):
    for i in graph[node]:
        rmNode(graph, i)
    graph[node] = None

N = int(input())
nodeList = list(map(int, sys.stdin.readline().rstrip().split()))
removeNode = int(input())

graph = list([] for _ in range(N))
for i in range(N):
    if(nodeList[i] == -1):
        continue
    graph[nodeList[i]].append(i)

cnt = 0
if(removeNode in graph[nodeList[removeNode]]):
    graph[nodeList[removeNode]].remove(removeNode)
rmNode(graph, removeNode)
for i in graph:
    if(i != None and len(i) == 0):
        cnt += 1

print(cnt)