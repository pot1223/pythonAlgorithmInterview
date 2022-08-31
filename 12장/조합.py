
import itertools
def returnCombination(n : int , k : int) : 
  return list(itertools.combinations(range(1 , n+1) , k))
 
returnCombination(4,2)

# itertools 모듈 사용하지 않고 풀이 

def returnCombination(n : int , k : int) : 
  results = []
  def dfs(elements , start : int , k : int) :
    if k == 0 :
      results.append(elements[:])
    for i in range(start , n+1) : 
      elements.append(i)
      dfs(elements , i+1 , k-1)
      elements.pop()
  dfs([] , 1 , k)
  return results
  
 
returnCombination(4 , 2)
