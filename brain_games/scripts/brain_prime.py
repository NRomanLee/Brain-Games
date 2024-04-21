#!/usr/bin/env python3
from brain_games.games.prime import get_number_and_prime_answer
from brain_games.the_engine import run_game


def play_prime():
    run_game(get_number_and_prime_answer,
             'Answer "yes" if given number is prime. Otherwise answer "no".')


def main():
    play_prime()


if __name__ == '__main__':
    main()
