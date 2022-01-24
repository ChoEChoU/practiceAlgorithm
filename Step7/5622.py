w = input()

time = 0

for i in range(0, len(w)):
  a = w[i]

  if a in ["A", "B", "C"]:
    time += 2
  elif a in ["D", "E", "F"]:
    time += 3
  elif a in ["G", "H", "I"]:
    time += 4
  elif a in ["J", "K", "L"]:
    time += 5
  elif a in ["M", "N", "O"]:
    time += 6
  elif a in ["P", "Q", "R", "S"]:
    time += 7
  elif a in ["T", "U", "V"]:
    time += 8
  elif a in ["W", "X", "Y", "Z"]:
    time += 9
  else:
    time += 10

time += len(w)

print(time)