def letterCombination(digits : str) :
  my_dict = {'2' : "ABC" , '3' : "DEF" , '4' : "GHI" , '5' : "JKL" , '6' : "MNO" , '7' : "PQRS" , '8' : "TUV" , '9' : "WXYZ"}
  result = [""]
  for d in digits : 
      q = list(result) # deepcopy
      result = []
      for s in q : 
        for c in my_dict[d].lower() : 
          result.append(s + c)
  return result  


letterCombination("234")
