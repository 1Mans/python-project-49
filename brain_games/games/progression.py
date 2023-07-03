import random

DESCRIPTION = 'What number is missing in the progression?'
START_RANGE = (0, 30)
STEP_RANGE = (2, 5)
PROGRESSION_LENGTH_RANGE = (5, 10)


def generate_progression(length, start_range=START_RANGE, step_range=STEP_RANGE):
    start = random.randint(start_range[0], start_range[1])
    step = random.randint(step_range[0], step_range[1])
    progression = list(range(start, start + length * step, step))
    return progression


def build_question(progression, hidden_index):
    progression_with_hidden = progression.copy()
    progression_with_hidden[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_hidden))
    return question, str(progression[hidden_index])


def get_question_and_answer(progression_length_range=PROGRESSION_LENGTH_RANGE):
    progression_length = random.randint(progression_length_range[0], progression_length_range[1])
    progression = generate_progression(progression_length)
    hidden_index = random.randint(0, progression_length - 1)
    question, answer = build_question(progression, hidden_index)
    return question, answer
