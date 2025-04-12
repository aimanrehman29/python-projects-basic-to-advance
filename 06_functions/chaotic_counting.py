import random

DONE_LIKELIHOOD = 0.3 

def done():
    """
    Randomly return True with a likelihood of DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    """
    Prints numbers from 1 to 10, checking 'done()' before each print.
    If done() returns True, the function stops and returns.
    """
    for i in range(1, 11):  
        if done():  
            return  
        print(i, end=" ")  

def main():
    # Prompt the user for input to start counting
    start_input = input("Do you want to start the counting process? (yes/no): ")
    if start_input.lower() == "yes":
        print("I'm going to count until 10 or until I feel like stopping, whichever comes first.", end=" ")
        chaotic_counting() 
        print("I'm done.")
    else:
        print("Okay, maybe next time!")

if __name__ == '__main__':
    main()
