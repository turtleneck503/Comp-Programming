x = int(input())
days = "31"

if x == 2:
    days = "28"
elif x == 4 or x == 6 or x == 9 or x == 11:
    days = "30"

print(days)