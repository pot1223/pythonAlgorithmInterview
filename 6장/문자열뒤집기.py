# 슬라이싱을 이용한 풀이 

def reverse_str(s:str):
  reverse=[]
  reverse = str[::-1]
  return reverse

# 위치 포인터를 이용한 풀이

def reverse_pt(s:str):
  p1 = 0
  p2 = len(s)-1
  while p1<p2:
    s[p1],s[p2] = s[p2],s[p1]
    p1+=1
    p2-=1
  return s
  
 #파이썬 메소드를 이용한 풀이 
 
 def reverse_md(s:str):
  s.reverse()
  return s 
  
