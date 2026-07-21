#Calculator
print("=" * 60)
print("WELCOME TO THE ULTIMATE PYTHON CALCULATOR")
print("=" * 60)

def line():
    print("-" * 60)

def title():
    line()
    print("Choose an operation")
    line()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Percentage")
    print("9. Average")
    print("10. Maximum")
    print("11. Minimum")
    print("12. Square")
    print("13. Cube")
    print("14. Square Root")
    print("15. Exit")
    line()

def addition(a, b):
    result = a + b
    print("Addition Result =", result)

def subtraction(a, b):
    result = a - b
    print("Subtraction Result =", result)

def multiplication(a, b):
    result = a * b
    print("Multiplication Result =", result)

def division(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    else:
        result = a / b
        print("Division Result =", result)

def modulus(a, b):
    if b == 0:
        print("Cannot perform modulus by zero.")
    else:
        result = a % b
        print("Modulus Result =", result)

def power(a, b):
    result = a ** b
    print("Power Result =", result)

def floor_division(a, b):
    if b == 0:
        print("Cannot perform floor division by zero.")
    else:
        result = a // b
        print("Floor Division Result =", result)

def percentage(a, b):
    if b == 0:
        print("Cannot calculate percentage.")
    else:
        result = (a / b) * 100
        print("Percentage =", result, "%")

def average(a, b):
    result = (a + b) / 2
    print("Average =", result)

def maximum(a, b):
    if a > b:
        print("Maximum =", a)
    elif b > a:
        print("Maximum =", b)
    else:
        print("Both numbers are equal.")

def minimum(a, b):
    if a < b:
        print("Minimum =", a)
    elif b < a:
        print("Minimum =", b)
    else:
        print("Both numbers are equal.")

def square(a):
    print("Square =", a * a)

def cube(a):
    print("Cube =", a * a * a)

def square_root(a):
    if a < 0:
        print("Square root of negative number is not supported.")
    else:
        guess = a
        if guess == 0:
            print("Square Root = 0")
            return
        for i in range(20):
            guess = (guess + a / guess) / 2
        print("Square Root =", guess)

while True:
    title()

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input.")
        continue

    if choice == 15:
        print("Thank you for using the calculator.")
        break

    if choice in [12, 13, 14]:
        try:
            num = float(input("Enter a number: "))
        except:
            print("Invalid number.")
            continue

        if choice == 12:
            square(num)

        elif choice == 13:
            cube(num)

        elif choice == 14:
            square_root(num)

    else:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except:
            print("Invalid number.")
            continue

        if choice == 1:
            addition(num1, num2)

        elif choice == 2:
            subtraction(num1, num2)

        elif choice == 3:
            multiplication(num1, num2)

        elif choice == 4:
            division(num1, num2)

        elif choice == 5:
            modulus(num1, num2)

        elif choice == 6:
            power(num1, num2)

        elif choice == 7:
            floor_division(num1, num2)

        elif choice == 8:
            percentage(num1, num2)

        elif choice == 9:
            average(num1, num2)

        elif choice == 10:
            maximum(num1, num2)

        elif choice == 11:
            minimum(num1, num2)

        else:
            print("Invalid choice.")

    line()
    input("Press Enter to continue...")
