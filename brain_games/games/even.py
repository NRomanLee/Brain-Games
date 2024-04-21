import random
from brain_games.the_engine import run_game


def is_even(num):
    return num % 2 == 0


def get_num_and_even_answer():
    num = random.randint(1, 20)
    correct_answer = 'yes' if is_even(num) else 'no'
    return num, correct_answer


def play_game():
    run_game(get_num_and_even_answer,
             '''Answer "yes" if the number is even, otherwise answer "no".''')
