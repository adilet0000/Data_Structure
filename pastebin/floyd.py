def min_total_cost():
   inf = float('inf')
   letters = {'a': 0, 'b': 1, 'c': 2}
   n = 3
   dist = [[inf] * n for _ in range(n)]

   for i in range(n):
      dist[i][i] = 0

   dist[letters['a']][letters['c']] = 1
   dist[letters['a']][letters['b']] = 3
   dist[letters['b']][letters['c']] = 1
   dist[letters['b']][letters['a']] = 2
   dist[letters['c']][letters['a']] = 4
   dist[letters['c']][letters['b']] = 1

   for k in range(n):
      for i in range(n):
         for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
               dist[i][j] = dist[i][k] + dist[k][j]

   costs = []
   for target in range(n):
      total = 0
      for src in range(n):
         total += dist[src][target]
      costs.append(total)

   return min(costs)

print(min_total_cost())
