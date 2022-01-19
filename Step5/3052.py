list = set([])

for i in range(0, 10):
    a = int(input())
    remainder = a % 42

    list.add(remainder)
    
print(len(list))