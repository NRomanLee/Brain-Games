#!/usr/bin/env python3
from brain_games.games.calc import get_math_expression_and_result
from brain_games.engine import run_game


def main():
    run_game(get_math_expression_and_result,
             '''What is the result of the expression?''')


if __name__ == '__main__':
    main()
