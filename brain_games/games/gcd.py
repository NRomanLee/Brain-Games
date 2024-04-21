import math
import random


def get_gcd(first_num, second_num):
    return math.gcd(first_num, second_num)


def get_number_pair_and_gcd():
    first_num = random.randint(1, 20)
    second_num = random.randint(1, 20)
    gcd = get_gcd(first_num, second_num)
    nums = f'{first_num} {second_num}'

    return nums, str(gcd)
