year = int(input())

if (year % 400 == 0):
    print("1")
else:
    if (year % 100 == 0):
        print("0")
    else:
        if (year % 4 == 0):
            print("1")
        else:
          print("0")