import random


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def generate_progression_hidden_num():
    PROGRESSION_LENGTH = 10
    start_num, step = random.randint(1, 100), random.randint(1, 10)
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_to_replace = random.randint(0, PROGRESSION_LENGTH - 1)
    hidden_num = progression[index_to_replace]
    progression[index_to_replace] = '..'

    missed = " ".join(map(str, progression))
    return missed, str(hidden_num)
