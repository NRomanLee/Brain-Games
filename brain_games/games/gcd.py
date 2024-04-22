import math
import random
MIN_NUMBER = 1
MAX_NUMBER = 20


def get_number_pair_and_gcd():
    first_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_num = random.randint(MIN_NUMBER, MAX_NUMBER)
    gcd = math.gcd(first_num, second_num)
    num = f'{first_num} {second_num}'

    return num, str(gcd)
