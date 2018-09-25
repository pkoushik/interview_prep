import collections

def bfs(graph, node):
    seen_nodes = set([node])
    queue = collections.deque([node])
    while queue:
        v = queue.popleft()
        print(v)
        for n in graph[v]:
            if n not in seen_nodes:
                seen_nodes.add(n)
                queue.append(n)
# graph = {0: [1,2], 1: [2,0], 2: []}
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"]
        }
bfs(graph, graph.keys()[0]) 
