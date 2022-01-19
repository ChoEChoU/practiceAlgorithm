a = int(input())

for i in range(0, a):
    ox = input()
    stack = []
    result = 0
    for j in range(0, len(ox)):
        if ox[j] == "O":
            stack.append(ox[j])
            result += len(stack)
        else:
            stack.clear()
    print(result)
