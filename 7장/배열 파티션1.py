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
