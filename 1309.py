N = int(input())

# 0, 1, 2 없고 왼쪽 오른쪽
graph = list([0] * 3 for _ in range(2))

graph[0][0] = 1
graph[0][1] = 1
graph[0][2] = 1

for i in range(1, N):
    graph[i%2][0] = graph[(i-1)%2][0] + graph[(i-1)%2][2] + graph[(i-1)%2][2]
    graph[i%2][1] = graph[(i-1)%2][0] + graph[(i-1)%2][2]
    graph[i%2][2] = graph[(i-1)%2][0] + graph[(i-1)%2][1]


print(sum(graph[(N-1)%2]) % 9901)
