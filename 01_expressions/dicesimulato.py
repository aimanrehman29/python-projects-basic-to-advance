import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2

def main():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    
    for _ in range(3):
        dice1, dice2 = roll_dice()  
        print(f"Roll: {dice1}, {dice2}") 
        
    print("die1 in main() is: " + str(die1))

if __name__ == '__main__':
    main()
