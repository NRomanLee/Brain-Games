import random


def get_math_expression_and_result():
    first_num = random.randint(1, 20)
    second_num = random.randint(1, 20)
    action = random.choice(['+', '-', '*'])
    if action == '+':
        result = first_num + second_num
    elif action == '-':
        result = first_num - second_num
    elif action == '*':
        result = first_num * second_num
    expression = f'{first_num} {action} {second_num}'
    return expression, str(result)
