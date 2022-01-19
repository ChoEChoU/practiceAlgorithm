n = int(input())

list = [n for n in map(int, input().split())]

list.sort()

max = list[len(list)-1]

min = list[0]

print(min, max)