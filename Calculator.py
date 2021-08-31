from art import logo
print(logo)

def add(n1, n2):
    sum = n1 + n2
    return sum

def subtract(n1, n2):
    difference = n1-n2
    return difference

def multiply(n1, n2):
    product = n1*n2
    return product

def divide(n1, n2):
    quotient = n1/n2
    return quotient

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number: "))

    for symbol in operations:
        print(symbol)

    should_stop = False
    while not should_stop:
        operation_choice = input("Pick an operation: ")

        num2 = float(input("What's the next number: "))

        calculation_function = operations[operation_choice]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_choice} {num2} = {answer}")
        try_again = input(f"Type 'y' to continue trying with {answer}, or type 'n' to start a new calculator. ").lower()
        if try_again == "n":
            should_stop = True
            calculator()
        elif try_again == "y":
            num1 = answer
        else:
            print("You pressed the wrong key.")

calculator()