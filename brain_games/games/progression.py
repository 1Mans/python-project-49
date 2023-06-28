import random

DESCRIPTION = 'What number is missing in the progression?'



def generate_progression(length):
    start = random.randint(0, 30)
    step = random.randint(2, 5)
    progression = list(range(start, start + length * step, step))
    return progression


def build_question(progression, answer):
    progression_with_hidden = progression.copy()
    hidden_index = random.randint(0, len(progression) - 1)
    progression_with_hidden[hidden_index] = '..'
    question = ' '.join(map(str, progression_with_hidden))
    return question, str(progression[hidden_index])


def get_question_and_answer():
    progression_length = random.randint(5, 10)
    progression = generate_progression(progression_length)
    question, answer = build_question(progression, progression_length)
    return question, answer


