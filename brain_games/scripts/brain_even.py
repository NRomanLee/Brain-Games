#!/usr/bin/env python3
from brain_games.games.even import get_num_and_even_answer
from brain_games.engine import run_game


def main():
    run_game(get_num_and_even_answer,
             '''Answer "yes" if the number is even, otherwise answer "no".''')


if __name__ == "__main__":
    main()
