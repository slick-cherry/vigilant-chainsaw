# Ultra-stupid calculator
# When your math skills are worse than Internet Explorer's speed

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Divide by 0? Seriously?!"
        return num1 / num2
    else:
        return "Unsupported operation. Did you just make that up?"

if __name__ == "__main__":
    print("Enter two numbers and an operation (+, -, *, /)")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation: ")

    result = calculate(num1, num2, operation)
    print(f"Result: {result}")

    # Meme for good measure
    print("\nMath: Exists")
    print("My brain: 'Error 404 - Skill not found'")
