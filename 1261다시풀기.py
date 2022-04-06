import sys

# 다시 풀기

def dfs(x, y, cnt):
    global visit, graph, direct, min
    visit[x][y] = True

    if(graph[x][y] == 1):
        cnt += 1

    if(x == N-1 and y == M-1):
        if(cnt < min):
            min = cnt
        visit[x][y] = False
        return

    for i, j in direct:
        if(0 <= x + i < N and 0 <= y + j < M):
            if(visit[x + i][y + j] is False):
                dfs(x + i, y + j, cnt)
    visit[x][y] = False

M, N = map(int, input().split())
graph = list([0] * M for _ in range(N))

for i in range(N):
    graph[i][:M] = map(int, list(sys.stdin.readline().rstrip()))

direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visit = list([False] * M for _ in range(N))

min = 100000

dfs(0, 0, 0)

print(min)
