#!/usr/bin/env python3

from brain_games.games.prime import get_number_and_prime_answer
from brain_games.engine import run_game


def main():
    run_game(get_number_and_prime_answer,
             'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    main()
