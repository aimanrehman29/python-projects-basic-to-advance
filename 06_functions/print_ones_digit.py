def print_ones_digit(num):
    """
    This function takes an integer num and prints its ones digit.
    """
    ones_digit = num % 10  
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))
    
    print_ones_digit(num)

if __name__ == '__main__':
    main()
