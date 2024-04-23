import random


PROGRESSION_LENGTH = 10
INSTRUCTION = 'What number is missing in the progression?'
START_MIN_NUM = 1
START_MAX_NUM = 100
STEP_MIN_NUM = 1
STEP_MAX_NUM = 10


def generate_progression(start, step, length):
    return list(range(start, start + step * length, step))


def get_question_and_answer():
    start_num = random.randint(START_MIN_NUM, START_MAX_NUM)
    step = random.randint(STEP_MIN_NUM, STEP_MAX_NUM)
    progression = generate_progression(start_num, step, PROGRESSION_LENGTH)

    index_to_replace = random.randint(0, PROGRESSION_LENGTH - 1)
    hidden_num = progression[index_to_replace]
    progression[index_to_replace] = '..'

    missed = " ".join(map(str, progression))
    return missed, str(hidden_num)
