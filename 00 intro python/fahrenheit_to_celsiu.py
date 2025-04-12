def main ():
    print("This program help you to convert Fahrenheit to Celsius")
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit : "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C .")

if __name__ == '__main__':
    main()