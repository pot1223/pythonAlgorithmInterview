# 투 포인터 사용 풀이 

lst = [0,1,0,2,1,0,1,3,2,1,2,1]
def rainwaterTrapping(s:list):
  if not s:
    return 0
  volume = 0
  left, right = 0 , len(s)-1
  left_max, right_max = s[left],s[right]
  while left<right:
    left_max, right_max =max(left_max,s[left]),max(right_max, s[right])
    if left_max <= right_max:
      volume += left_max -s[left]
      left +=1 
    else:
      volume += right_max - s[right]
      right -=1
  return volume
rainwaterTrapping(lst)

# 스택 사용 풀이 

def trap(height:list):
  stack= []
  volume = 0
  for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
      top = stack.pop()
      if not len(stack):
        break
      distance = i - stack[-1] -1 
      waters = min(height[i],height[stack[-1]]) - height[top]
      volume += distance * waters
    stack.append(i)
  return volume
