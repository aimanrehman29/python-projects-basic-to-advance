def main ():
    num1 = int(input("Enter the dividend : "))
    num2 = int(input("Enter the divisor : "))
    quotient = num1 // num2
    remainder = num1 % num2
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

if __name__ == '__main__':
    main()