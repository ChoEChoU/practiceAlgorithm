c = int(input())
for i in range(0, c):

    num = [n for n in input().split()]

    sum = 0

    for j in range(1, len(num)+1):
        num[j-1] = int(num[j-1])
        sum += num[j-1]
    
    average = sum // num[0]

    result = 0

    for k in range(1, len(num)):
        if num[k] >= average:
            result += 1

    result = result / num[0] * 100

    print('%.3f' %result + "%")