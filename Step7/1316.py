n = int(input())
result = 0
for i in range(0, n):
  w = input()
  wList = []
  flag = True
  for j in range(0, len(w)):
    if w[j] in wList:
      if w[j-1] != w[j]:
        flag = False
      else:
        wList.append(w[j])
    else:
      wList.append(w[j])
  if flag == True:
    result += 1
  
print(result)