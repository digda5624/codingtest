# 깝치지마 현승구 여사건 접근하지마

def dfs(visit, x, y, count, depth, N):
    global probd, prob
    # N번 완료
    if (depth > N):
        return

    #N번 전에 삐끗
    if(visit[x][y] is True):
        minus = 1
        for i in range(4):
            minus = minus * (probd[i] ** count[i])
        prob -= minus
        return

    visit[x][y] = True
    depth += 1
    global direct
    for i in range(4):
        j, k = direct[i]
        count[i] = count[i] + 1
        dfs(visit, x + j, y + k, count, depth, N)
        count[i] = count[i] - 1
    visit[x][y] = False


direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
count = [0, 0, 0, 0]
prob = 1.0

N, r, l, d, u = list(map(int, input().split()))
probd = [r/100, l/100, d/100, u/100]


visit = list([False] * (2 * N + 1) for _ in range(2 * N + 1))

dfs(visit, N, N, count, 0, N)
print(prob)
