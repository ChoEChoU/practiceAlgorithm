t = int(input())
for i in range(0, t):
    r, s = input().split()
    for j in range(0, len(s)):
        print(s[j] * int(r), end = "")
    print("")