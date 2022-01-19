list = []
max = 0


for i in range(0,9):
    a = int(input())
    list.append(a)

    if (max <= a):
        max = a

print(max)
print(list.index(max)+1)