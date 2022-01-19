a = int(input())
b = int(input())
c = int(input())

numList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

mul = a * b * c

strMul = str(mul)

for i in range(0, len(strMul)):
    numList[int(strMul[i])] += 1

for j in numList:
    print(j)