# 743. Network Delay Time
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

import heapq

def networkDelayTime(times, n, k):
   graph = {i: [] for i in range(1, n + 1)}
   for u, v, w in times:
      graph[u].append((v, w))
   
   heap = [(0, k)]
   dist = {i: float('inf') for i in range(1, n + 1)}
   dist[k] = 0

   while heap:
      time, node = heapq.heappop(heap)
      for neighbor, weight in graph[node]:
         if dist[neighbor] > time + weight:
            dist[neighbor] = time + weight
            heapq.heappush(heap, (dist[neighbor], neighbor))
   
   max_time = max(dist.values())
   return max_time if max_time != float('inf') else -1

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))


# Example 1:
# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1








# 1631. Path With Minimum Effort
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

def minimumEffortPath(heights):
   m, n = len(heights), len(heights[0])
   heap = [(0, 0, 0)]
   efforts = [[float('inf')] * n for _ in range(m)]
   efforts[0][0] = 0
   directions = [(-1,0),(1,0),(0,-1),(0,1)]

   while heap:
      effort, x, y = heapq.heappop(heap)
      if x == m - 1 and y == n - 1:
         return effort
      for dx, dy in directions:
         nx, ny = x + dx, y + dy
         if 0 <= nx < m and 0 <= ny < n:
            new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
            if efforts[nx][ny] > new_effort:
               efforts[nx][ny] = new_effort
               heapq.heappush(heap, (new_effort, nx, ny))

print(minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))


# Example 1:
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
# Example 2:

# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
# Example 3:


# Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
 








# 787. Cheapest Flights Within K Stops
# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.


def findCheapestPrice(n, flights, src, dst, k):
   graph = {i: [] for i in range(n)}
   for u, v, w in flights:
      graph[u].append((v, w))
   
   heap = [(0, src, 0)]
   dist = dict()

   while heap:
      cost, node, stops = heapq.heappop(heap)
      if node == dst:
         return cost
      if stops > k:
         continue
      for neighbor, price in graph[node]:
         if (neighbor, stops) not in dist or cost + price < dist[(neighbor, stops)]:
            dist[(neighbor, stops)] = cost + price
            heapq.heappush(heap, (cost + price, neighbor, stops + 1))
   
   return -1

print(findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))


# Example 1:

# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
# Output: 700
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
# Example 2:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
# Output: 200
# Explanation:
# The graph is shown above.
# The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
# Example 3:


# Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The graph is shown above.
# The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

