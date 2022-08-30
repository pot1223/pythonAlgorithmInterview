def permute(nums : list) :
  results = []
  prev_elements = []
  def dfs(elements) : 
    if len(elements) == 0 : 
      results.append(prev_elements[:]) 
    for e in elements : 
      next_elements = elements[:] # elements 리스트를 new_elements 리스트로 copy 한다 
      next_elements.remove(e) # next_elements 리스트에 e요소값을 삭제한다 

      prev_elements.append(e)
      dfs(next_elements)
      prev_elements.pop()
  dfs(nums)
  return results    

nums = [1 , 2 , 3]
permute(nums)

# itertools 모듈 사용 (실무에서 사용한다)

import itertools

def permute(nums : list) : 
  return list(itertools.permutations(nums))
