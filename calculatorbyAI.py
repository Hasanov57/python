def operations():
    print("+\n-\n/\n*")

def calculate(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    else:
        print("Invalid operation")
        return None
    return result

def calculation():
    num1 = float(input("What's the first number?\n"))
    operations()
    operation = input("Select the operation:\n")
    num2 = float(input("What's the second number?\n"))
    return calculate(num1, operation, num2)

while True:
    result = calculation()
    
    while True:
        answer = input(f"Do you want to continue with the result {result}, or start a new calculation? (y/n)\n")
        if answer == "y":
            operations()
            operation = input("Select the operation:\n")
            num2 = float(input("What's the next number?\n"))
            result = calculate(result, operation, num2)
        else:
            break
