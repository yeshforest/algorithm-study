n=int(input())
#1일때 1
#2 (6*1)+1 =7
#3  (6*2)+7=19
#4 (6*3)+19
t=1
cnt=1
while t<n:
  t += 6*cnt
  cnt += 1
print(cnt)


#t와 n이 왜 같으면 안되는가?
#입력이 7이면 답이 2인데 cnt값은 3이나온다.
#경계값에 주의