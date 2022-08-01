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
