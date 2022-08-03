def longPalindrom(s:str): # 직접 푼 풀이 
  lst1 = []
  lst2 = []
  result=''
  for i in range(len(s)):
    fcpointer = i
    while s[i] == s[fcpointer]:
      fcpointer+=1
      if fcpointer == len(s):
        break
    if fcpointer >0:
      lst1.append(s[i:fcpointer])
  mlst1 = max(lst1,key =len)
    
  for i in range(len(s)-1):
     fpointer = i-1
     lpointer = i+1
     while s[fpointer] ==  s[lpointer]:
       fpointer -=1 
       lpointer +=1
       if fpointer <= 0 or lpointer == len(s):
         break
     lst2.append(s[fpointer+1:lpointer])
  mlst2= max(lst2,key =len)     
  result = max(mlst1,mlst2, key=len)
  if len(result) ==1:
    print("팰린드롬이 없습니다")
  else:
    return result

words = "1234575480"
longPalindrom(words)


def longestPalindrome(s:str): #  또 다른 방법 (책 풀이)
  def expand(left:int, right:int):
    while left >=0 and right <=len(s) and s[left] ==s[right-1]:
      left -=1
      right +=1
    return s[left+1:right-1]
  if len(s) < 2 or s == s[::-1]:
    return s 
  result=''
  for i in range(len(s)-1):
    result = max(result, expand(i,i+1),expand(i,i+2), key =len)
  return result 

words = "1234575480"
longestPalindrome(words)






