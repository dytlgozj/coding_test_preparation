# dfs using recursion

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end = " ")

    for vertex in graph[start]:
        if not visited[vertex]:
            dfs(graph, vertex, visited)

graph = [
    [],
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
