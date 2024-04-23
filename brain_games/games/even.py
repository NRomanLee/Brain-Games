import random


MIN_NUMBER = 1
MAX_NUMBER = 20
INSTRUCTION = '''Answer "yes" if the number is even, otherwise answer "no".'''


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer
