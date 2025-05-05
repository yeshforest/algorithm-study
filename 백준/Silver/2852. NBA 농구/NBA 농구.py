n = int(input())

one = 0 # 1팀이 이긴 시간
two = 0 # 2팀이 이긴 시간
flag = 0  # 1팀이 득점시 +1, 2팀이 득점시 -1

for i in range(n):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    
    if team == '1':
        if flag == 0: # 비기고 있으면
            one += 48*60 - (60*m+s) #  전체 - 비긴시간

        flag += 1 # 팀1이 득점했으므로 flag 증가
        if flag == 0: # 팀 1 득점이후 다시 동점이 된 경우
            if two > 0: # 2팀이 이기고 있었다면
                two = two - (48*60 - (60*m+s)) # 방금 동점을 만들었기때문에 비긴시간 빼줌
            
            
    else:
        if flag == 0:
            two += 48*60 - (60*m+s) # 동점에서 팀2가 득점시 비긴시간 빼줌
        
        flag -= 1
        if flag == 0:
              # 팀2 득점 이후 동점이 된 경우
            if one > 0:
              # 팀1이 이전에 리드 중이었다면
              # 방금 시점부터 경기 끝까지 빼줌
                one = one - (48*60 - (60*m+s))
                
                
print('{:0>2}:{:0>2}'.format(one//60,one%60))
print('{:0>2}:{:0>2}'.format(two//60,two%60))