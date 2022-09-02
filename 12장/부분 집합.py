from typing import *
def setReturn(lst : list) -> List[List[int]] :
  result = []
  def dfs(index , path) :
    result.append(path) 
    for i in range(index , len(lst)) : 
      dfs(i+1 , path + [lst[i]]) # [a] + [b] 는 [a , b]가 된다 
  dfs(0 , [])
  return result 

nums = [1 ,2 ,3]
setReturn(nums)
