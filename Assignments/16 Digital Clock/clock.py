mins = int(input())

hours = mins // 60

mins %= 60

while hours >= 24:
    hours -= 24

print(hours, mins)