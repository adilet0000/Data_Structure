n = int(input())
mat = [] * n
for i in range(n):
	mat.append(list(map(int, input().split())))

# Алгоритм Флойда
# (Время: 1 сек. Память: 16 Мб Сложность: 36%)
# Полный ориентированный взвешенный граф задан матрицей смежности. Постройте матрицу кратчайших путей между его вершинами. Гарантируется, что в графе нет циклов отрицательного веса.

# Входные данные
# В первой строке входного файла INPUT.TXT записано единственное число N (1 ≤ N ≤ 100) - количество вершин графа. В следующих N строках по N чисел - матрица смежности графа (j-ое число в i-ой строке соответствует весу ребра из вершины i в вершину j). Все числа по модулю не превышают 100. На главной диагонали матрицы - всегда нули.
# def floyd_warshall(graph):
#     for i in range(len(graph)):
#         for j in range(len(graph)):
#             for k in range(len(graph)):
#                 if i == j or j == k or i == k:
#                     continue
#                 if graph[j][k] > graph[j][i] + graph[i][k]:
#                     graph[j][k] = graph[j][i] + graph[i][k]
#     return graph

# floyd_warshall(mat)

# for i in mat:
#    print(*i)








# Самый длинный путь
# (Время: 1 сек. Память: 16 Мб Сложность: 42%)
# Дан ориентированный взвешенный граф, рёбрам которого приписаны некоторые неотрицательные веса (длины).

# Требуется найти две вершины, кратчайший путь между которыми имеет наибольшую длину.

# Входные данные
# В первой строке входного файла INPUT.TXT задано число вершин N (3 ≤ N ≤ 50). Далее идёт матрица смежности графа, то есть N строк, в каждой из которых записано N чисел. j-ое число в i-ой строке матрицы смежности задает длину ребра, ведущего из i-й вершину в j-ую. Длины могут принимать любые значения от от 0 до 106. Гарантируется, что на главной диагонали матрицы стоят нули.

# def floyd_warshall(graph):
#     for i in range(len(graph)):
#         for j in range(len(graph)):
#             for k in range(len(graph)):
#                 if i == j or j == k or i == k:
#                     continue
#                 if graph[j][k] > graph[j][i] + graph[i][k]:
#                     graph[j][k] = graph[j][i] + graph[i][k]
#     return graph

# ans = 0

# graph = floyd_warshall(mat)
# for i in range(len(graph)):
#     for j in range(len(graph)):
#         if i != j and graph[i][j] > ans:
#             ans = graph[i][j]
# print(ans)









# Алгоритм Флойда - 2
# (Время: 1 сек. Память: 16 Мб Сложность: 39%)
# Дан ориентированный взвешенный граф. Вам необходимо найти пару вершин, кратчайшее расстояние от одной из которых до другой максимально среди всех пар вершин.

# Входные данные
# В первой строке входного файла INPUT.TXT записано единственное число N (1 ≤ N ≤ 100) - количество вершин графа. В следующих N строках по N чисел - матрица смежности графа, где -1 означает отсутствие ребра между вершинами, а любое неотрицательное число - присутствие ребра данного веса. Элементы матрицы - целые числа от -1 до 100. На главной диагонали матрицы - всегда нули. Гарантируется, что в графе есть хотя бы одно ребро.

for i in range(n):
   for j in range(n):
      if mat[i][j] == -1:
         mat[i][j] = float('inf')

def floyd_warshall(graph):
   for k in range(len(graph)):
      for i in range(len(graph)):
         for j in range(len(graph)):
            if graph[i][k] + graph[k][j] < graph[i][j]:
               graph[i][j] = graph[i][k] + graph[k][j]
   return graph

floyd_warshall(mat)

max_dist = -1
for i in range(n):
   for j in range(n):
      if i != j and mat[i][j] != float('inf'):
         max_dist = max(max_dist, mat[i][j])

print(max_dist)
