y, x = map(int,input().split())
block = list(map(int,input().split()))
answer = 0
 
for i in range(1, x-1): # 처음, 마지막은 제외하고
    left = max(block[ :i]) # 본인 기준 최대값의 왼쪽
    right = max(block[i+1: ]) # 본인 기준 최대값의 오른쪽
    m = min(left, right)  # 그중 최솟값만큼
    if m > block[i]: # 현재블록보다 높으면
        answer += m - block[i] # 누적합
 
print(answer)