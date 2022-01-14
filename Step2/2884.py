H,M = map(int, input().split())

allMinute = H * 60 + M
alarmClock = 0

if allMinute <= 45:
    H = 23
    M = 60
    allMinute = H * 60 + M + allMinute
    
    alarmClock = allMinute - 45

else:
    alarmClock = allMinute - 45

H = alarmClock // 60
M = alarmClock % 60

if H == 24:
  H = 0

print(H, M)