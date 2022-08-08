# 나눗셈을 이용한 풀이 

lst = [1,2,3,4]
def product_array(s:list):
  result = []
  i= 0 
  k= 1
  while i < len(s):
    k *= s[i]
    i+=1
  for i in range(len(s)):
    result.append(k//s[i])
  return result
product_array(lst)

# 나눗셈을 이용하지 않고 copy()를 이용한 풀이 

lst = [1,2,3,4]
def product_array(s:list):
  stack = []
  t = 0
  reflection = s.copy()
  for i in range(len(s)): 
    s = reflection.copy()
    s.remove(s[i])
    j= 0 
    k= 1
    while j < len(s):
      k *= s[j]
      j+=1
    stack.append(k)
  return stack 
product_array(lst)
