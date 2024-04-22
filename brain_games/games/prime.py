import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_number_and_prime_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    prime_check = is_prime(number)
    answer = 'yes' if prime_check else 'no'
    return str(number), answer
