def double(num):
    """
    Takes a number and returns the result of multiplying it by 2.
    """
    return num * 2

def main():
    num = int(input("Enter a number: "))
    
    result = double(num)
    
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()
