import math  # for square root

def main():
    print("This program calculates the hypotenuse of a right triangle.")
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    bc = math.sqrt(ab**2 + ac**2 )
    print("The length of BC (the hypotenuse) is: " + str(bc))

if __name__ == '__main__':
    main()