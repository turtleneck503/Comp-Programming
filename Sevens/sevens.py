"""
Name: Jonathan Perry
Class: Computer Programming 1
Section: A2
"""

#Import statements

#User Functions

#main function
def main():
    SEVEN = 7
    for num in range(1,50,1):
        if num % SEVEN == 0:
            print("clap")
        else:
            print(num)

#conditional execution
if __name__ == "__main__":
    main()