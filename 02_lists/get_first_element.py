def get_first_element(lst):
     print("First element:", lst[0])

def main ():
     my_list =[]
     n = int(input("Enter number of elements: "))

     for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
     get_first_element(my_list)

if __name__ == '__main__':
  main()