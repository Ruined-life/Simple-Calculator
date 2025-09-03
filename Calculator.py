import time


def calculate():
    number1 = input('Type the first number: ')
    number2 = input('Type the second number: ')
    operator = input('Type the operator: ')

    #addition
    if operator == '+':
        return int (number1) + int (number2)

    #subtraction
    if operator == '-':
        return int(number1) - int(number2)

    #division
    if operator == '/':
        return float(number1) / float(number2)

    #multiply
    if operator == 'x' or operator == '*' or operator == 'X':
        return int(number1) * int(number2)

    else:
        print("Invalid operator")
        
  

while True:
    time.sleep(0.5)
    print(calculate())