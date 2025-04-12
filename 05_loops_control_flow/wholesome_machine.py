def main():
    correct_affirmation = "I am capable of doing anything I put my mind to."
    
    while True:
        user_input = input("Please type the following affirmation: ")
        
        if user_input == correct_affirmation:
            print("That's right! :)")
            break 
        else:
            print("Hmmm That was not the affirmation.") 

if __name__ == "__main__":
    main()
