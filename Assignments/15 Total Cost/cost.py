dollars = int(input())
cents = int(input())
cupcakes = int(input())

cost = (dollars + (cents / 100)) * cupcakes

cents = int((cost * 100) % 100)
dollars = int(cost - cents / 100)

print(dollars, cents)