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
graph = {0: [1,2], 1: [2,0], 2: []}
bfs(graph, 0)
