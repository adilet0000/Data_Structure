def dfs_components_from_edge_list_matrix(edge_list, n):
   # создаём матрицу смежности
   mat = [[0] * n for _ in range(n)]
   for u, v in edge_list:
      mat[u][v] = 1
      mat[v][u] = 1

   visited = [0] * n
   components = []

   def dfs(v, comp):
      visited[v] = 1
      comp.append(v)
      for i in range(n):
         if mat[v][i] == 1 and not visited[i]:
            dfs(i, comp)

   for i in range(n):
      if not visited[i]:
         comp = []
         dfs(i, comp)
         components.append(comp)

   return components

def dfs_components_from_edge_list_adj_list(edge_list, n):
   # создаём список смежности
   graph = {i: [] for i in range(n)}
   for u, v in edge_list:
      graph[u].append(v)
      graph[v].append(u)

   visited = set()
   components = []

   def dfs(v, comp):
      visited.add(v)
      comp.append(v)
      for neighbor in graph[v]:
         if neighbor not in visited:
            dfs(neighbor, comp)

   for i in range(n):
      if i not in visited:
         comp = []
         dfs(i, comp)
         components.append(comp)

   return components

edge_list = [
   (0, 1),
   (1, 2),
   (3, 4)
]
n = 5


print(dfs_components_from_edge_list_matrix(edge_list, n))
print(dfs_components_from_edge_list_adj_list(edge_list, n))
