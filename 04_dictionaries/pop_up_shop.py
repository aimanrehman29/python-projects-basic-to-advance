def main():
    fruit_prices = {
        'apple': 2.5,
        'durian': 10.0,
        'jackfruit': 3.0,
        'kiwi': 1.5,
        'rambutan': 4.0,
        'mango': 5.0
    }

    total_cost = 0  

   
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += quantity * price 

    
    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
