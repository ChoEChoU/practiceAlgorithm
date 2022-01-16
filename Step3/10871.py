n, x = map(int, input().split())

list = [n for n in input().split()]

for j in list:
    if (x > int(j)):
        print(j, end=" ")