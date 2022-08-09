# 브루트 포스법으로 풀이

lst = [7,1,5,3,6,4]
def maxinterest(s:list):
  presult=[]
  result=[]
  for i in range(len(s)-1):
    for j in range(i,len(s)):
      presult.append(s[j]-s[i])
    result.append(max(presult))
  return max(result) 

maxinterest(lst)
