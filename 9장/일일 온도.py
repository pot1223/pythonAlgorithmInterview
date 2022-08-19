T = [73,74,75,71,69,72,76,73,74]


def TemperatureWarm(lst = list):
  result=[]
  n=0
  for i in range(len(lst)):
    for j in range(i,len(lst)):
      n+=1
      if lst[i] < lst[j]:
        result.append(n-1) 
        break
    n = 0
    if lst[i] >= lst[j]:
      result.append(n)
  
  return result 

TemperatureWarm(T)
