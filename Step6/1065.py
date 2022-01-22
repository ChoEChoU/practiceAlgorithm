def check(num):
  if num < 100:
    return True
  else:
    strNum = str(num)
    gap = 0
    flag = True
    first = True
    for i in range(1, len(strNum)):
      gapRe = int(strNum[i-1]) - int(strNum[i])
      if first is True:
        gap = gapRe
        first = False
      else:
        if gap != gapRe:
          flag = False
    return flag



n = int(input())

result = 0

for i in range(1, n+1):
  if check(i) is True:
    result += 1

print(result)