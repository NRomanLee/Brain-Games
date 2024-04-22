#!/usr/bin/env python3
from brain_games.games.progression import generate_progression_hidden_num
from brain_games.engine import run_game


def main():
    run_game(generate_progression_hidden_num,
             'What number is missing in the progression?')


if __name__ == '__main__':
    main()
