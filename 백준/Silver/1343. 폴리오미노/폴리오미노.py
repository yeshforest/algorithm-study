# AAAA 
# BB
# X만 덮을려고 한다.
# XXXXXX

board = list(input())
for i in range(0,len(board)-3):
  isXCnt= 0
  for j in range(i,i+4):
    if board[j] == 'X':
      isXCnt +=1
  if isXCnt ==4:
    for j in range(i,i+4):
      board[j] = 'A'
    #isXCnt = 0



for i in range(0,len(board)-1):
  isXCnt = 0
  for j in range(i,i+2):
    if board[j] == 'X':
      isXCnt +=1
  if isXCnt == 2:
    for j in range(i,i+2):
      board[j] = 'B'
    isXCnt = 0 


if 'X' in board:
  print(-1)
else:
  answer = ''.join(board)
  print(answer)