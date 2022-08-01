# 정규표현식 사용1 

import re 

paragraph = "Bod hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def findMode(s:str,b=list):

  s= re.sub("[^a-zA-Z]",' ',s).lower().split()
  removenum = 0
  numlst =[]
  findnum = 0 
  findlst = []

  for i in range(len(b)):
    for j in range(len(s)):
      if b[i] == s[j]:
        removenum += 1
    numlst.append(removenum)
    for replay in range(int(numlst[i])):
        s.remove(b[i])
    num = 0
  for i in range(1,len(s)):
    if s.count(s[i]) < s.count(s[i-1]):
      return s[i-1]

findMode(paragraph,banned)

# 정규표현식과 리스트 컴프리핸션 사용 

def mostCommonWord(paragraph : str, banned= List[str]) -> str:
  words = [word for word in re.sub(r'[^\w]','',paragraph).lower().split() if word not in banned]
  counts = collections.Counter(words) #  Counter 모듈을 사용해서 Counter 객체를 만든다 
  return counts.most_common(1)[0][0] # Counter객체의 most_common(n번째 값) 을 사용하면 가장 많이 쓰인 값이 [(값,개수)] 형태의 리스트로 반환된다 





