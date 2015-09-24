def add(number_list):
    answer = 0
    for num in number_list:
        answer += num
    return answer


def subtract(number_list):
    answer = 0
    first = True
    for num in number_list:
        if first:
            answer += num
            first = False
        else:
            answer -= num
    return answer


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2
