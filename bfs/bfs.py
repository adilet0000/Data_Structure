# Hika's code BFS implementation
from collections import deque

def bfs_sh(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = path + [neighbor]
                queue.append(new_path)
    
    return None
g = {
    '0': ['1','2'],
    '1': ['0','6'],
    '2': ['0','3','4','5'],
    '3': ['2','4'],
    '4': ['2','5', '7'],
    '5': ['2','4','9'],
    '6': ['1','8','9','10'],
    '7': ['4'],
    '8': ['6'],
    '9': ['6','5'],
    '10': ['6']
}

print(bfs_sh(g, '0', '10'))