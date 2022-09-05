from typing import *
import collections
import heapq

def networkDelayTime(times : List[List[int]] , N : int , K : int) -> int : 
  graph = collections.defaultdict(list)
  for u , v , w in times : 
    graph[u].append((v , w))
  Q = [(0 , K)]
  dist = collections.defaultdict(int)
  while Q : 
    time , node = heapq.heappop(Q)
    if node not in dist : 
      dist[node] = time 
      for v , w in graph[node] : 
        alt = time + w
        heapq.heappush(Q , (alt , v))
  if len(dist) == N :
    return max(dist.values())
  return -1 

times = [[2 , 1 , 1] , [2 , 3 , 1] , [3 , 4 , 1]]
networkDelayTime(times , 4 , 2)
