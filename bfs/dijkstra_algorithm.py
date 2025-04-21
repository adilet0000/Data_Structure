import heapq

# Дан ориентированный взвешенный граф. Для него вам необходимо найти кратчайшее расстояние от вершины S до вершины F.

# Входные данные
# В первой строке входного файла INPUT.TXT записаны три числа: N, S и F (1 ≤ N ≤ 100; 1 ≤ S, F ≤ N), где N - количество вершин графа. В следующих N строках записаны по N чисел - матрица смежности графа, где число в i-ой строке j-ом столбце соответствует ребру из i в j: -1 означает отсутствие ребра между вершинами, а любое неотрицательное целое число (от 0 до 100) - наличие ребра данного веса. На главной диагонали матрицы всегда записаны нули.

# Выходные данные
# В выходной файл OUTPUT.TXT необходимо вывести искомое расстояние или -1, если пути между указанными вершинами не существует.

def dijkstra(matrix, start, end):
   n = len(matrix)
   dist = [float('inf')] * n
   visited = [False] * n
   dist[start] = 0

   heap = [(0, start)]

   while heap:
      current_dist, u = heapq.heappop(heap)

      if visited[u]:
         continue
      visited[u] = True

      for v in range(n):
         weight = matrix[u][v]
         if weight != -1 and not visited[v]:
            if dist[v] > current_dist + weight:
               dist[v] = current_dist + weight
               heapq.heappush(heap, (dist[v], v))

   return -1 if dist[end] == float('inf') else dist[end]

n = 3
s = 1
f = 3
matrix = [
   [0, 1, -1],
   [-1, 0, 2],
   [4, -1, 0]
]

result = dijkstra(matrix, s - 1, f - 1)
print(result)
