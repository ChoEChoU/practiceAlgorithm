x = int(input())
y = int(input())

if (0 < x and 0 < y):
    print("1")
elif (0 < x and y < 0):
    print("4")
elif (x < 0 and y < 0):
    print("3")
else:
    print("2")