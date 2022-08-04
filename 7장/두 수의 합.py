# 브루트 포스법으로 해결한 문제로 시간복잡도가 0(n2)나 된다 

def returnsumindex(lst : list, target : int ):
  flist = []
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
       if lst[i]+lst[j] == target:
         flist.append([i,j])
  if len(flist) ==0:
    print("실패했습니다")
  else:
    return flist 

nums =[2,7,11,15]
target =100
returnsumindex(nums,target)

# in을 이용한 풀이 
def twoSum(nums:list, target:int):
   for i, n in enumerate(nums): 
      complement = tanget - n 
      if complement in nums[i+1:]: #in 연산을 이용한 풀이는 0(n2) 시간복잡도라도 브루트 포스법보다 훨씬 더 가볍고 빠르게 풀 수 있다 
        return nums.index(n), nums[i+1:].index(complement)+(i+1)
     
# dictionary를 이용한 풀이 

def twoSum(nums:list, target: int):
  nums_map={}
  for i, num in enumerate(nums):
    nums_map[num] = i # num값을 키로 하고 i를 인덱스로 하는 딕셔너리를 만든다 
  for i, num in enumerate(nums):
    if target-num in nums_map and i != nums_map[target -num]: #전체적인 시간복잡도는 0(n)이 된다 
      return nums.index(num), nums_map[target-num] # 딕셔너리로 조회하므로 평균적으로 시간복잡도가 0(1)이 된다 
     
# dictionary를 이용한 풀이2

def twoSum(nums:list, target: int):
  nums_map ={}
  for i, num in enumerate(nums):
    if target -num in nums_map:
      return [nums_map[target-num],i]
    nums_map[num] = i 
      
      
      
      
      
