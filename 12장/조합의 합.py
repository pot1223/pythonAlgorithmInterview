def sumTarget(lst : list , target : int) :
  result = []
  def dfs(csum , index , path) : # csum은 합 갱신 , index는 순서 , path는 지금까지의 탐색 경로 
    if csum < 0 :
      return
    if csum == 0 : 
      result.append(path)
      return 
    for i in range(index , len(lst)) : 
      dfs(csum - lst[i] , i , path + [lst[i]])
  dfs(target , 0 ,[])
  return result   

lst = [2 ,3 , 6, 7]
sumTarget(lst , 7)
