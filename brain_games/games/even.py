import random

TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():
    question: int = random.randint(1, 50)
    answer = 'yes' if question % 2 == 0 else 'no'
    return question, answer
