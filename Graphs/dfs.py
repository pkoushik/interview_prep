def dfs(graph, v, path=[]):
    path.append(v)
    for n in graph[v]:
        if n not in path:
            path = dfs(graph, n, path)
    return path

graph = {1: [2, 3],
         2: [4, 5],
         3: [5],
         4: [6],
         5: [6],
         6: [7],
         7: []}

print(dfs(graph, 1))
