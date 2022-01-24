a = input()

upperA = a.upper()
setA = set([])


for i in range(0, len(upperA)):
    setA.add(upperA[i])

maxA = ""
cnt = 0
for j in setA:
    if cnt < upperA.count(j):
      cnt = upperA.count(j)
      maxA = j
    elif cnt == upperA.count(j):
      maxA = "?"

print(maxA)