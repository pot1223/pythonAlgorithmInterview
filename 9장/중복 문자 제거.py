import collections

def removeDuplicateLetters(s : str):
   counter, seen, stack = collections.Counter(s), set(),[]
   for char in s:
     counter[char] -= 1 # collections.Counter타입의 객체는 {문자1 : 문자1개수, 문자2 : 문자 2개수, ...} 형태로 나타나며 counter[문자1] 은 문자 1의 개수가 출력된다  
     if char in seen: #  이미 stack에 들어간 문자는 스킵한다, 중복 제거 
       continue
     while stack and char < stack[-1]  and  counter[stack[-1]] >0 : # stack이 존재하고 stack의 제일 마지막 요소가 해당 문자보다 사전식으로 뒤에 있고 stack의 제일 마지막 요소가 s문자열에 존재하면 수행한다 
        seen.remove(stack.pop()) # stack에서 제일 마지막 요소를 제거 후 그 요소를 seen에서 제거 
     stack.append(char)
     seen.add(char)
   return ''.join(stack) 

removeDuplicateLetters("cbacdcbc")
