from collections import deque
# 큐 자료구조를 사용하기 위해서 deque 라이브러리를 사용한다
# 방문하는 방식에 대한 정의이다. dfs는 끝까지 찍었다가 나오는 거라면 bfs는 트리의 높이로 구분짓는 느낌

def bfs(graph, root, visit):
    visit[root] = True
    queue = deque([root])
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if(visit[i] == False):
                queue.append(i)
                visit[i] = True

graph = [
    [], # 0 번 노드는 없다고 생각하고 코드를 작성한다.
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
