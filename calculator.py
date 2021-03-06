"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def num_converter(number_text):
    try:
        number = int(number_text)
    except ValueError:
        number = float(number_text)
    return number

while True:
    user_input = raw_input("> ")
    tokenized_input = user_input.split()
    
    operator = tokenized_input[0]

    if operator.lower() == "q":
        break

    num1 = num_converter(tokenized_input[1])
    try:
        num2 = num_converter(tokenized_input[2])
    except IndexError:
        pass

    if operator == "+":
        print add(num1, num2)
    elif operator == "-":
        print subtract(num1, num2)
    elif operator == "*":
        print multiply(num1, num2)
    elif operator == "/":
        print divide(num1, num2)
    elif operator == "square":
        print square(num1)
    elif operator == "cube":
        print cube(num1)
    elif operator == "pow":
        print power(num1, num2)
    elif operator == "mod":
        print mod(num1, num2)
    else:
        print "That is not an accepted input! Try again."
