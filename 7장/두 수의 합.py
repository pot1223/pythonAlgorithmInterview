def returnsumindex(lst : list, target : int ):
  flist = []
  for i in range(len(lst)):
    for j in range(i+1,len(lst)):
       if lst[i]+lst[j] == target:
         flist.append([i,j])
  if len(flist) ==0:
    print("실패했습니다")
  else:
    return flist 

nums =[2,7,11,15]
target =100
returnsumindex(nums,target)
