from typing import *
import collections
def reconfigureSchedule(ticket : List[List[str]]) -> List[str]:
  graph = collections.defaultdict(list)
  for a , b in sorted(ticket) : 
    graph[a].append(b)
  route = [] 
  def dfs(a): # dfs("JFK") -> dfs("MUC") -> dfs("LHR") -> dfs("SFO") -> dfs("SJC") 가 되어 route는 ["SJC" , "SFO" , "LHR" , "MUC" , "JFK"] 가 된다
    while graph[a] : 
      dfs(graph[a].pop(0))
    route.append(a)
  dfs("JFK")
  return route[::-1]
ticket = [["MUC" , "LHR"] , ["JFK" , "MUC"] , ["SFO" , "SJC"] , ["LHR" , "SFO"]]
reconfigureSchedule(ticket)
