def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def get_number(prompt):
    """Helper function to safely get a number from user."""
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid number! Please enter a valid number.")

def main():
    print("======== SIMPLE CALCULATOR ========")
    
    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting Calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose 1–5.")
            continue

        # Input numbers
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        # Perform operation
        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print("Result:", result)

if __name__ == "__main__":
    main()
+