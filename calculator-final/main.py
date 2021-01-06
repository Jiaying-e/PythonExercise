#Calculator
from art import logo
#add
def add (n1, n2):
    return n1 + n2

#substract
def substract (n1, n2):
    return n1 + n2


#multiply
def multiply (n1, n2):
    return n1 * n2

#divide
def devide (n1, n2):
    return n1 / n2

operations = {"+": add,
"-": substract,
"*": multiply,
"/": devide
}

def calculator():
    print(logo)
    num1 = int(input("The first number: "))
    for symbol in operations:
        print (symbol)
    should_continue = True
    while should_continue:


        num2 = int(input("The next number: "))
        operation = input("Pick an operation from the line above")
        calculation_operation = operations[operation]
        answer = calculation_operation(num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input(f"type 'y' if continue calculating with {answer}, and type 'n' to start new calculator") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()