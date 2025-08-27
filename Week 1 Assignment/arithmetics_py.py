# Enhanced Basic Calculator Program

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid number. Please try again.")

def get_operation():
    valid_ops = ['+', '-', '*', '/']
    while True:
        op = input("Enter operation (+, -, *, /): ").strip()
        if op in valid_ops:
            return op
        else:
            print("❌ Invalid operation. Please choose from +, -, *, or /.")

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "⚠️ Error: Cannot divide by zero."
        else:
            return a / b

def main():
    print("🧮 Welcome to the Fancy Calculator 🧮")
    
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = calculate(num1, num2, operation)

        if isinstance(result, str):  # Handle division by zero error
            print(result)
        else:
            print(f"✅ Result: {num1} {operation} {num2} = {round(result, 2)}")

        again = input("\nDo you want to calculate again? (y/n): ").lower()
        if again != 'y':
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
