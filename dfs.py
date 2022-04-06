def dfs(graph, node, visit):
    visit[node] = True
    print(node, end=" ")

    for i in graph[node]:
        if(visit[i] == False):
            dfs(graph, i, visit)

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

dfs(graph, 1, visited)

# 방문한 노드를 표시할 리스트 필요 참 거짓으로 하면 좋겠다.
# 그래프를 표시하기 위해서는 2차원 배열 필요, 노드 번호에 각각 인접한 노드 번호들이 리스트로 들어감
# print를 언제하느냐에 따라서 결과가 달라질수도 있다.
# 재귀를 사용함으로써 스택자료형을 대신한다.