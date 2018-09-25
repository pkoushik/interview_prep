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

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"]
        }
print(dfs(graph, graph.keys()[0]))
