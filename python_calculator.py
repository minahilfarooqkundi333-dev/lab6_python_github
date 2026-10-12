
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Check Even/Odd")
print("6. Calculate Percentage")
print("7. Exit")
while True:
    
    choice = int(input("Enter one of the options: "))
    if choice == 1:
        print("ADDITION:", num1 + num2)
    elif choice == 2:
        print("SUBTRACTION:", num1 - num2)
    elif choice == 3:
        print("MULTIPLICATION:", num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("DIVISION:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    elif choice == 5:
        if num1 % 2 == 0:
            print("Number 1 is even")
        elif num1==0:
            print("It is zero")
        else:
            print("Number 1 is odd")

        if num2 % 2 == 0:
            print("Number 2 is even")
        elif num2==0:
            print("It is zero")
        else:
            print("Number 2 is odd")
    elif choice == 6:
        if num2 != 0:
            percentage = (num1 / num2) * 100
            print("PERCENTAGE:", percentage, "%")
        else:
            print("Error: Cannot calculate percentage with zero.")
    elif choice == 7:
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1 to 7.")
        choice = int(input("Enter one of the options: "))
    
   
         
