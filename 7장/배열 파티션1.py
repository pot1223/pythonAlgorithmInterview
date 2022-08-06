# 내림차순 정렬 후 2개 요소마다 min값 더하기  

lst = [2,5,7,4,3,2]
def arraypartition(s:lst):
  s.sort(reverse= True)
  i=0
  k=0 
  while i < len(s)-1:
    a = s[i]
    b = s[i+1]
    k += min(a,b)
    i+=2
  return k  
    
arraypartition(lst)

# 내림차순 정렬 후 짝수 번째 합 계산 

lst = [2,5,7,4,3,2]
def arraypartition(s:lst):
  s.sort(reverse= True)
  sum = 0
  for i,n in enumerate(s):
    if i % 2 ==0:
      sum += n
  return sum 

arraypartition(lst)


# 오름차순 정렬 후 파이썬다운 방법 사용 

lst = [2,5,7,4,3,2]
def arraypartition(s:lst):
  return sum(sorted(s)[::2])

arraypartition(lst)
