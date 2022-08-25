def findJewel(J : str, S : str):
  table = {} 
  count = 0 
  for s in S:
    if s not in table:
      table[s] = 1 
    else:
      table[s] += 1
  for j in J:
    if j in table:
      count += table[j]
  return count 

findJewel("aA" , "aAAbbbb")
