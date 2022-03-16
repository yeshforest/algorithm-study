a=[0]*10
cnt=0
#결과를 배열에 담아 서로 비교?
for i in range(10):
  n=int(input())
  a[i]=n%42
for i in range(42):
  if i in a:
    cnt += 1

print(cnt)
#if A in B : B안에 A가 있으면 true
#if A not in B: B안에 A가 없다면 true
#B에는 리스트, 튜플, 문자열을 사용할 수 있다.