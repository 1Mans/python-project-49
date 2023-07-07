import random

DESCRIPTION = 'What number is missing in the progression?'
START_MIN = 0
START_MAX = 30
STEP_MIN = 2
STEP_MAX = 5
LENGTH_MIN = 5
LENGTH_MAX = 10


def generate_progression(length, first_term, difference):
    progression = [first_term + i * difference for i in range(length)]
    return progression


def build_question(progression, hidden_index):
    progression_with_hidden = progression.copy()
    progression_with_hidden[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_hidden))
    return question, str(progression[hidden_index])


def get_question_and_answer():
    progression_length = random.randint(LENGTH_MIN, LENGTH_MAX)
    first_term = random.randint(START_MIN, START_MAX)
    difference = random.randint(STEP_MIN, STEP_MAX)
    progression = generate_progression(progression_length,
                                       first_term, difference)
    hidden_index = random.randint(0, progression_length - 1)
    return build_question(progression, hidden_index)
