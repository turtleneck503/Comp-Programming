a = int(input())


x = a % 10
y = (a // 10) % 10
z = ((a // 10) // 10) % 10

a = x + y + z

print(a)