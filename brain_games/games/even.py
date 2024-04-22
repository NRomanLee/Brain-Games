import random


MIN_NUMBER = 1
MAX_NUMBER = 20


def is_even(num):
    return num % 2 == 0


def get_num_and_even_answer():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer
