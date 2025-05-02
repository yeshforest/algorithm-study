h,w = map(int,input().split())
answer = []
for i in range(h): # 한 줄 입력 ( c..c )
  arr = list(input())

  for j in range(w): # j == 1
    finish = False
    if arr[j] == 'c': 
      answer.append(0)
      continue
    for k in range(j,-1,-1): # for k in range(1,0,-1)
      # c를 만나면 k 저장
      if arr[k] == 'c': # arr[0] = c
        answer.append(j-k) # 1이 되어야하는거 아닌가?
        finish = True
        break # 만나면 해당 for문은 종료.
    if not finish:
      #끝까지 k가 c가 아니면  
      answer.append(-1)
      continue
  for i in answer:
    print(i, end=" ")
  print("")
  answer = []
