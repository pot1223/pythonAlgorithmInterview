lst = ["eat", "tea", "tan" ,"ate" ,"nat","bat"]

def anagram(s:list):
  analst = []
  flist=[]
  result = []
  for i in range(len(s)):
    analst.append("".join(sorted(s[i])))
  for i in range(len(analst)):
    flist.append([ s[j] for j in range(len(analst)) if analst[i]==analst[j]])
  for value in flist:  # for 문으로 리스트 중복제거 
    if value not in result: 
        result.append(value)
  return result
anagram(lst)
