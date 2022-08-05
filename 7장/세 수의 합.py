nums = [-1,0,1,2,-1,4]

def threesum(s:list):
  lst = []
  finalist = []
  fpointer = 0 
  lpointer = len(s)-1
  while fpointer < lpointer-1:
    findnum = 0-(s[fpointer]+s[lpointer])
    if findnum in s[fpointer+1:lpointer]:
      lst.append(s[fpointer])
      lst.append(s[lpointer])
      lst.append(findnum)
      finalist.append(lst)
      lst = []
    lpointer -=1 
  return finalist 
threesum(nums)
