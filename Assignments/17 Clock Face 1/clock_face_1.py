hours = int(input())
minutes = int(input())
seconds = int(input())

degrees = (hours * 30) + (minutes / 2) + (seconds / 120)

while degrees >= 360:
    degrees -= 360

print(degrees)