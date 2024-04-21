#!/usr/bin/env python3
from brain_games.games.calc import get_math_expression_and_result
from brain_games.the_engine import run_game


def calc_game():
    run_game(get_math_expression_and_result,
             '''What is the result of the expression?''')


def main():
    calc_game()


if __name__ == '__main__':
    main()
