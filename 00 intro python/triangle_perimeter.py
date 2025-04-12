def main ():
    side1: float = float(input("What is the length of side a? "))
    side2: float = float(input("What is the length of side b? "))
    side3: float = float(input("What is the length of side c? "))

    print("The perimeter of the triangle is " + str(side1 + side2 + side3))

if __name__ == '__main__':
    main()