def get_last_element(lst):
    a = lst[len(lst) - 1]  # Or lst[-1]
    print("Last element:", a)

def main():
    my_list = []
    n = int(input("Enter number of elements: "))

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    get_last_element(my_list)

if __name__ == '__main__':
    main()
