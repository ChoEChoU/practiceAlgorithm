n = int(input())

numlist = [n for n in input().split()]

maxnum = 0

for k in range(0, len(numlist)):
  numlist[k] = int(numlist[k])
  if numlist[k] > maxnum:
    maxnum = numlist[k]

for i in range(0, len(numlist)):
    numlist[i] = int(numlist[i]) / maxnum * 100

sum = 0

for j in numlist:
    sum += j

average = sum / len(numlist)

print(average)