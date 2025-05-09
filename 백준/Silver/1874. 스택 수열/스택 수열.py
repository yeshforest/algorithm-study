# target이 나오기 전까지 push, 나오면 pop
# pop한거 다른 배열에 담아두기
# traget+1, 최상위값이 target과 같으면 pop, 다르면 종료.
import sys
input = sys.stdin.readline

N = int(input())
arr = []
stack=[] # 스택
answers=[]
for _ in range(N):
  arr.append(int(input()))

i = 1
target = 0
isStack = True

 
for target in arr:
  while i<=target: # target과 같을때까지
    stack.append(i) # push
    answers.append('+')
    i+=1

  if stack[-1] == target: # stack의 최상단값이 target값과 같으면
    stack.pop()
    answers.append("-")
  else:
      isStack = False
      break


if isStack:
  for answer in answers:
    print(answer)
else:
  print("NO")