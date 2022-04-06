
def star(graph, N):
    if(N == 3):
        graph[0][:3] = [1] * 3
        graph[1][:3] = [1, 0, 1]
        graph[2][:3] = [1] * 3
        return

    star(graph, N // 3)
    temp = N // 3
    for i in range(3):
        for j in range(3):
            if(i == 1 and j == 1):
                continue
            for k in range(temp):
                graph[temp * i + k][temp * j:temp * (j + 1)] = graph[k][:temp]

N = int(input())
graph = [[0] * N for _ in range(N)]
star(graph, N)

for i in range(N):
    for j in range(N):
        if(graph[i][j] == 1):
            print("*", end='')
        else:
            print(" ", end='')
    print()


