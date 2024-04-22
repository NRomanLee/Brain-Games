#!/usr/bin/env python3

from brain_games.games.gcd import get_number_pair_and_gcd
from brain_games.engine import run_game


def main():
    run_game(get_number_pair_and_gcd,
             'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()
