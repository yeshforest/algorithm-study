# 숫자랑 문자 엮어서 2차원배열로 저장. 그리고 찾아서 그 숫자에 +3
arr =  ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sen = input()
sum =0
# 타겟글자가 포함된 요소를 찾기
for i in range(len(sen)):
  result = [(p,x) for p, x in enumerate(arr) if sen[i] in x]
  sum += result[0][0]+ 2 + 1

print(sum)