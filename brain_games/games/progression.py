import random

DESCRIPTION = 'What number is missing in the progression?'
START_MIN = 0
START_MAX = 30
STEP_MIN = 2
STEP_MAX = 5



def generate_progression(length):
    start = random.randint(START_MIN, START_MAX)
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = list(range(start, start + length * step, step))
    return progression


def build_question(progression, hidden_index):
    progression_with_hidden = progression.copy()
    progression_with_hidden[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_hidden))
    return question, str(progression[hidden_index])


def get_question_and_answer():
    progression_length = random.randint(5, 10)
    progression = generate_progression(progression_length)
    hidden_index = random.randint(0, len(progression) - 1)
    question, answer = build_question(progression, hidden_index)
    return question, answer
