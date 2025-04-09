n = 10
n += 1
vis = [0] * n

def dfs(x):
   global n, vis
   vis[x] = 1
   for i in range(n):
      if vis[x][i] == 1 and vis[i] == 0:
         dfs(i)
   return




mat = [[]] * n

m = 7

for i in range(n):
   mat[i] = [0] * n
for i in range(m):
   x, y = map(int, input().split())
   mat[x][y] = 1
   mat[y][x] = 1

for i in range(1, n):
   print(i, end=' ')
   print(mat[i])


dfs(1)