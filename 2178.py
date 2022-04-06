# 미로 탐색 최단거리 문제
import sys
from collections import deque
def bfs(graph, x, y, visit, cost):
    vector = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    queue = deque([(x, y)])
    visit[x][y] = True
    cost[x][y] = 1
    while(queue):
        x1, y1 = queue.popleft()
        for i in vector:
            a = x1 + i[0]
            b = y1 + i[1]
            if(0 <= a < N and 0 <= b < M and graph[a][b] == '1' and visit[a][b] == False):
                queue.append((a, b))
                cost[a][b] = cost[x1][y1] + 1
                visit[a][b] = True

    return

N, M = map(int, input().split())
graph = []
cost = [[0] * M for _ in range(N)]
visit = [[False] * M for _ in range(N)]
for i in range(N):
    graph.append(list(sys.stdin.readline()))

bfs(graph, 0, 0, visit, cost)
print(cost[N-1][M-1])