import random


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_number_and_prime_answer():

    num = random.randint(1, 20)
    answer = 'yes' if is_prime(num) else 'no'
    return num, answer
