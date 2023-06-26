import random

TEXT = 'What number is missing in the progression?'


def question_and_answer():
    progression_length = random.randint(5, 10)
    progression = list(range(0, random.randint(30, 66), random.randint(2, 5)))
    if len(progression) > progression_length:
        progression = progression[:progression_length]
    answer = str(random.choice(progression))
    add_sep_to_progression = ' '.join(map(str, progression))
    question = add_sep_to_progression.replace(answer, '..', 1)
    return question, answer
