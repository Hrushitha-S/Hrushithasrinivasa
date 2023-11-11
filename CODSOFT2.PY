def cal():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))

    print("Select an operation:")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    operations = int(input("Enter your choice (1, 2, 3, or 4): "))
    if operations == 1:
        result = n1 + n2
        operation_sym = "+"
    elif operations == 2:
        result = n1 - n2
        operation_sym = "-"
    elif operations == 3:
        result = n1 * n2
        operation_sym = "*"
    elif operations == 4:
        result = n1 / n2
        operation_sym = "/"
    else:
        print("Invalid operation choice.")
        return
    print(f"{n1} {operation_sym} {n2} = {result}")
cal()