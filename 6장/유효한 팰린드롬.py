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
  return input == input[::-1] # 슬라이싱은 무지 빠르게 연산되므로 슬라이싱을 사용한 알고리즘이 속도 개선에 유리하다 


# 위치 포인터를 이용한 풀이 


def positionPalindrom(input: str):
  length = len(input)
  leftindex = 0 
  rightindex = 1
  for i in range(length):
    while input[i+leftindex].isalnum() == False:
      leftindex +=1 
      if leftindex == length:
        return True
    while input[length-i-rightindex].isalnum() == False:
      rightindex +=1
    if i+leftindex >= length-i-rightindex:
      break
    if input[i+leftindex].lower() != input[length-i-rightindex].lower():
      return False
  return True





