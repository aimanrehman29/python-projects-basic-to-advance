def main (): 
    lst=[0]
    given = input("Enter a value: ")
    while given :
        lst.append(given) 
        given= input("Enter a value: ")
    print("Here's the list:", lst)

if __name__ == '__main__':
    main()