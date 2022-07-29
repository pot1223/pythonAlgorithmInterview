inputstr = "A man, a plan. a canal: Panama"

# 리스트를 이용한 풀이

def palindrome(input: str):
  strlist = []
  for i in input:
    if i.isalnum():
      strlist.append(i.lower())
  while len(strlist) >1 :
    if strlist.pop(0) != strlist.pop(): # pop(0)는 시간복잡도가 0(n)이기 때문에 최적화를 시켜야 한다 
      return False
  return True


# 데큐를 이용한 풀이 

import collections
from typing import Deque
from collections import deque
inputstr = "A man, a plan. a canal: Panama"

def optimizePalindrome(input: str): 
  strlist:Deque = collections.deque # depue를 생성한다 
  flist = []
  for i in input:
    if i.isalnum():
       flist.append(i.lower()) 
  strlist= Deque(flist)   # 리스트를 depue로 변경한다 
  while len(strlist) >1 :
    if strlist.popleft() != strlist.pop(): # depue의 popleft() 메소드를 사용하면 시간복잡도가 0(1)이 된다   
      return False
  return True
optimizePalindrome(inputstr)

# 정규표현식을 이용한 풀이 

import re 

def Palindrome(input: str):
  input=input.lower()
  input = re.sub('[^a-z0-9]','',input) # a부터 z까지 문자, 0부터 9까지 숫자를 제외한 모든 기호는 삭제된다 
  return input == input[::-1]



