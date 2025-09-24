# 첫번째, 마지막/ 두번쨰 마지막-1, 이렇게 비교해서 모두 같으면 o /2했을떄 소수이면 가운데 무시

target = input()
printONE = True

for i in range(len(target)):
  if target[i] != target[len(target)-1-i]:
    print(0)
    printONE = False
    break

if printONE:
  print(1)