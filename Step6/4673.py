def d(n):
  num = 0
  num += n
  temp = num
  for i in range(0, len(str(n))):
    num += int(str(n)[i])

  return num

numList = []

for j in range(1, 10001):
    numList.append(j)

for i in range(1, 10000):
  if d(i) in numList:
      numList.remove(d(i))
      
for k in numList:
    print(k)