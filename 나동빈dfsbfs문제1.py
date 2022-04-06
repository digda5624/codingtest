#음료수 얼려먹기
# N*M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는
# 부분은 1로 표시됩니다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우
# 서로 연결되어 있는 것으로 간주합니다. 이때, 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스르림
# 의 갯수를 구하는 프로그램을 작성하시오
# 정보) 좌표 뒤집어서 생각해야 한다
# 상하좌우 처리 그냥 들어가게 해서 거기서 바로 빠져나오는 형식으로 하자

import sys
from collections import deque

def find(graph, node, visit, N, M):
    x, y = node
    list = []
    if (x < 0 and visit[x - 1][y] == False and graph[x - 1][y] == '0'):
        list.append((x - 1, y))
    if (y < 0 and visit[x][y - 1] == False and graph[x][y - 1] == '0'):
        list.append((x, y - 1))
    if (x < N-1 and visit[x + 1][y] == False and graph[x + 1][y] == '0'):
        list.append((x + 1, y))
    if (y < M-1 and visit[x][y + 1] == False and graph[x][y + 1] == '0'):
        list.append((x, y + 1))
    return list

def near(graph, x, y, visit, N, M):
    queue = deque([(x, y)])
    visit[x][y] = True

    while(queue):
        node = queue.popleft()
        for i in find(graph, node, visit, N, M):
            visit[i[0]][i[1]] = True
            queue.append(i)





# 그룹으로 묶여야한다. 0인거에 대해 체킹해서 돌려보면 되겠다.
N, M = map(int, input().split())
ice = []
for _ in range(N):
    ice.append(list(sys.stdin.readline().rstrip()))
visit = [[False] * M for _ in range(N)]
count = 0

for x in range(N):
    for y in range(M):
        if(ice[x][y] == '0' and visit[x][y] is False):
            near(ice, x, y, visit, N, M)
            count += 1

print(count)