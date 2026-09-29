miles_per_day = int(input())
total_miles = int(input())
days_of_travel: int

if total_miles % miles_per_day == 0:
    days_of_travel = total_miles // miles_per_day
else:
    days_of_travel =  total_miles // miles_per_day + 1

print(days_of_travel)