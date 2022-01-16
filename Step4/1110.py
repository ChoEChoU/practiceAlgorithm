a = int(input())

cnt = 0

c = a

if 0 <= a < 10:
    a *= 10
    cnt += 1

b = "0"

while(a != int(b)):
    first = int(c) // 10
    second = int(c) % 10

    sum = first + second

    sumSecond = sum % 10

    b = str(second) + str(sumSecond)
    cnt += 1
    
    c = b

print(cnt)
