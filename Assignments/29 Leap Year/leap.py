year = int(input())
answer = "COMMON"

if year%4 == 0:
    answer = "LEAP"
    if year%100 == 0:
        answer = "COMMON"
        if year%400 == 0:
            answer = "LEAP"


print(answer)