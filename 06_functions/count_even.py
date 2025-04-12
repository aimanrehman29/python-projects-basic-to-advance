def count_even(lst):
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "": 
            break
        else:
            try:
                num = int(user_input)
                lst.append(num)
            except ValueError:
                print("That's not a valid integer. Please try again.")
    
    even_count = sum(1 for num in lst if num % 2 == 0)
    
    print(f"The number of even numbers in the list is: {even_count}")

def main():
    numbers = []
    
    count_even(numbers)

if __name__ == '__main__':
    main()
