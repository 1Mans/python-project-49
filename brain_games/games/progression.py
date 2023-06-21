import random

TEXT = 'What number is missing in the progression?'


def question_and_answer():
    progression = list(range(0, random.randint(20, 56), random.randint(1, 10)))
    answer = str(random.choice(progression))
    add_sep_to_progression = ' '.join(map(str, progression))
    question = add_sep_to_progression.replace(answer, '..', 1)
    return question, answer
