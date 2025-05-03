from collections import defaultdict

T = int(input())
for _ in range(T) :
  N = int(input())
  num_list = list(map(int, input().split())) # 리스트
  num_cnt = defaultdict(int) # {}
  num_dict = defaultdict(list) # {}

  for num in num_list :
    num_cnt[num] += 1 # {1: 6, 2:4,3:6 ... }
  num_list = [ x for x in num_list if num_cnt[x] == 6 ]  # 6 이하인거 다 제거
  for idx, num in enumerate(num_list) :
    num_dict[num].append(idx) # {1[0] = 1, 3[0] = 2, } # 등수 매기기
  result = list(num_dict.keys()) # 1,3
  result.sort( key = lambda x : (sum(num_dict[x][:4]), num_dict[x][4], num_dict[x][5])) # 5번째 수로 비교해서 정렬 # 1[0~3]합, 5등점수, 6등점수
  print(result[0])