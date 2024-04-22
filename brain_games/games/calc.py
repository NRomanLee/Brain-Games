import random


MIN_NUMBER = 1
MAX_NUMBER = 20
ACTIONS = ['+', '-', '*']


def get_math_expression_and_result():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    action = random.choice(ACTIONS)
    if action == '+':
        result = first_num + second_num
    elif action == '-':
        result = first_num - second_num
    elif action == '*':
        result = first_num * second_num
    expression = f'{first_num} {action} {second_num}'
    return expression, str(result)
