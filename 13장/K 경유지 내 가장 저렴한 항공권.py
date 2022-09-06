from typing import *
import collections
import heapq

def findCheapesPrice(n : int , flights : List[List[int]] , src : int , dist : int , K : int) -> int :
  graph = collections.defaultdict(list)
  for u , v , w in flights:
    graph[u].append((v , w))
  Q = [(0 , src , K)]
  while Q : 
    price , node , K = heapq.heappop(Q)
    if node == dist : 
      return price
    if K >= 0 : # 남은 경유지 노드가 있을 경우 
      for v , w in graph[node] : 
        alt = price + w 
        heapq.heappush(Q , (alt , v , K-1))
  return -1 

edges = [[0 , 1 , 100] , [1 , 2 ,100] , [0 , 2 , 500]]

findCheapesPrice(n = 2 , flights = edges , src = 0 ,dist = 2 , K = 0)
