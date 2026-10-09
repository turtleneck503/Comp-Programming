month = int(input())
day = int(input())
days_in_month = 31

if month == 2:
    days_in_month = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days_in_month = 30

day += 1

if day > days_in_month:
    month += 1
    day -= days_in_month

if month > 12:
    month -= 12

print(month)
print(day)