import time
import names
import random

def print_name(x):
    timer = 5

    print("printing name in:")
    time.sleep(1)
    while timer != 0:
        print(timer)
        time.sleep(1)
        timer -= 1

    print(names.names[x])
    enter_number()

def enter_number():
    try:
        x = int(input("Enter a number, or 0 for a random name: ")) - 1
        name_count = len(names.names)
        if x > name_count - 1:
            print(f"Number too large, must be smaller than {name_count}")
            time.sleep(1)
            enter_number()
        elif x == -1:
            print_name(random.randint(0,name_count))
        elif x < 0:
            print("Number too small, must be at least 0")
            time.sleep(1)
            enter_number()
        else:
            print_name(x)
    except ValueError:
        print("No words")
        time.sleep(1)
        enter_number()

def get_random_name(x):
    """return a random name from the list of names"""
    return names.names[random.randint(0,x)]

enter_number()
