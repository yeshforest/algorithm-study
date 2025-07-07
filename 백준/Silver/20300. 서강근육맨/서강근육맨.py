# PT를 한번 받을 때 운동기구를 최대 두개까지만 선택 할 수 있다.
# N개의 운동기구. 근손실 정도가 한번당 M 넘지 않게. M의 최솟값?

N = int(input())
lost = list(map(int,input().split()))


lost.sort()


if (len(lost)%2) !=0: # 홀수이면
  maxNum = max(lost) # 최댓값
  end = len(lost)-2 # index 3
  start = 0 # index 0

  while start < end:
    start +=1
    end -=1
    maxNum = max(maxNum, lost[start] + lost[end])

  print(maxNum)
  
else: # 짝수이면
  start = 0
  end = len(lost)-1
  maxNum = 0
  while start < end:
    start +=1
    end -=1
    maxNum = max(maxNum, lost[start]+lost[end])
  print(maxNum)