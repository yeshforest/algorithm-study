# array에 저장해서 해당 인덱스랑 비교해서 숫자가 같게 만들어주기

chess = [1,1,2,2,2,8]

arr = list(map(int,input().split()))
answer=[]
for i in range(len(chess)):
  answer.append(chess[i]-arr[i])

print(*answer)