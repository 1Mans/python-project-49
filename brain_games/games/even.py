import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUM = 1
MAX_NUM = 50


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = random.randint(MIN_NUM, MAX_NUM)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
