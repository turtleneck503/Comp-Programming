x = int(input("enter number: "))

for i in range(1, x):

    output = ""
    
    if i % 3 == 0:
        output += "Fizz "
    if i % 5 == 0:
        output += "Buzz "
    if i % 7 == 0:
        output += "Boom "
    if i % 11 == 0:
            output += "Bang "
    if output == "":
        output = str(i)

    print(output)