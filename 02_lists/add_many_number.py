def add_many_numbers(numbers) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    total_so_far: int = 0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    a = int(input("Enter a digit: "))
    b = int(input("Enter another digit: "))
    
    lst = [a, b, 23]
    
    sum_of_numbers = add_many_numbers(lst)
    
    print("The sum of the numbers is:", sum_of_numbers)

if __name__ == '__main__':
    main()