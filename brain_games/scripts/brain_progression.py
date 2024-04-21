#!/usr/bin/env python3
from brain_games.games.progression import generate_progression_hidden_num
from brain_games.the_engine import run_game


def play_progression_game():
    run_game(generate_progression_hidden_num,
             'What number is missing in the progression?')


def main():
    play_progression_game()


if __name__ == '__main__':
    main()
