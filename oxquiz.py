n=int(input())#테스트케이스 갯수

for _ in range(n):
  s=list(input())
  sum=0
  cnt=1

  for i in range(len(s)):
    if s[i]=='O':# O이면
      sum=sum+cnt #cnt에 더하기
      cnt=cnt+1
    else: # X이면
      cnt=1  #0으로
    #연속된 O의 개수만큼 점수가 된다.
    #문자열이 연속돼있는건 어떻게 알지?
    #연속된 O가 나온 만큼 cnt값을 증가시킨다.
    
  print(sum)
    
  