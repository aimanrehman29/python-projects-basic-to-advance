MAX_LENGTH = 3

def shorten(lst):
    # Jab tak list ki length MAX_LENGTH se zyada hai
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Last element remove karo
        print("Removed:", removed)

def main():
    my_list = []
    n = int(input("Enter number of elements: "))

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)

    print("Original list:", my_list)
    shorten(my_list)
    print("Shortened list:", my_list)

if __name__ == '__main__':
    main()
