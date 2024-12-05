while True:
    def operations():
        return "+\n-\n/\n*"
    def calculation():
        num1=int(input("What's the first number?\n"))
        operation=input(f"select the operation\n {operations()}")
        num2=int(input("What's the second number?\n"))
        def add():
            result=float(num1)+float(num2)
            print(float(num1)," + ",float(num2)," = ")
            return result
        def subtract():
            result=float(num1)-float(num2)
            print(float(num1)," - ",float(num2)," = ")
            return result
        def divide():
            result=float(num1)/float(num2)
            print(float(num1)," / ",float(num2)," = ")
            return result
        def multiply():
            result=float(num1)*float(num2)
            print(float(num1)," * ",float(num2)," = ")
            return result
        if operation=="+":
            add=add()
            return add
        elif operation=="-":
            subtract=subtract()
            return subtract
        elif operation=="/":
            divide=divide()
            return divide
        else:
            multiply=multiply()
            return multiply
    calculation=calculation()
    print(calculation)  
    def y():
        num1=calculation
        operation=input(f"select the operation\n {operations()}")
        num2=int(input("What's the second number?\n"))
        def add():
            result=float(num1)+float(num2)
            print(float(num1)," + ",float(num2)," = ")
            return result
        def subtract():
            result=float(num1)-float(num2)
            print(float(num1)," - ",float(num2)," = ")
            return result
        def divide():
            result=float(num1)/float(num2)
            print(float(num1)," / ",float(num2)," = ")
            return result
        def multiply():
            result=float(num1)*float(num2)
            print(float(num1)," * ",float(num2)," = ")
            return result
        if operation=="+":
            add=add()
            return add
        elif operation=="-":
            subtract=subtract()
            return subtract
        elif operation=="/":
            divide=divide()
            return divide
        else:
            multiply=multiply()
            return multiply
    answer=input(f"Do you want to continue with the {calculation}, or start new calculation?(y/n)\n")
    if answer=="y":
        y=y()
        print(y)
    else:
        calculation=calculation()
        print(calculation)