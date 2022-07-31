import re 

def resort(s:list):
  resortlst1 = []
  resortlst2 = []
  for i in range(len(s)):
    if list(s[i][-1]) == re.findall('[a-zA-Z]',s[i][-1]):
      resortlst1.append(s[i])
      resortlst1.sort(key=lambda x :x.split()[1])
    else:
      resortlst2.append(s[i]) 
  finalresortlst = resortlst1 + resortlst2
  return finalresortlst
  
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
resort(logs)
