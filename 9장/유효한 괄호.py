def isValid(s:str):
  stack = [] 
  table = {
    ')' : '(',
    '}' : '{',
    ']' : '[',
  }
  for char in s: 
    if char not in table:
      stack.append(char)
    elif not stack or table[char] != stack.pop():
      return False
  return len(stack) == 0  # (가 stack에 들어간 후 stack.pop()을 하면 stack에는 아무것도 남지 않게 되고 (이 반환된다. table[)]은 (이므로 
# False를 리턴하지 않고 다음 인덱스로 이동한다. 전체 인덱스를 이동했을 때 괄호 순서가 유효하게 된다면 stack에는 아무것도 남지 않게 될 것이므로 len(stack) == 0 을 리턴한다 

isValid("(){}[]")
