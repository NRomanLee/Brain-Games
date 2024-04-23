import math
import random


MIN_NUMBER = 1
MAX_NUMBER = 20
INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    gcd = math.gcd(first_num, second_num)
    num = f'{first_num} {second_num}'

    return num, str(gcd)
