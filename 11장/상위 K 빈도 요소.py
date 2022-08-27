def overkFeature(lst : list, k : int):
  dic = {}
  for num in lst:
    if num not in dic:
      count =1 
      dic[num] = count
    else:
      dic[num] += 1
  return [ n for n in dic if dic[n]>=k] 
  
nums=[1,1,1,2,2,3]
overkFeature(nums,1)
