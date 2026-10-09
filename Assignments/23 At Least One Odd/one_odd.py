x = int(input())
y = int(input())
answer = "NO"
odd_nums = 0

def is_odd(num):
    if num%2 != 0:
        return True
    else:
        return False

if is_odd(x):
    odd_nums += 1

if is_odd(y):
    odd_nums += 1

if odd_nums > 0:
    answer = "YES"

print(answer)