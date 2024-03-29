import operator
import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUM = 1
MAX_NUM = 100


def get_question_and_answer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    symbols = ['+', '-', '*']
    symbols = random.choice(symbols)
    question = f'{num1} {symbols} {num2}'
    if symbols == '+':
        answer = operator.add(num1, num2)
    elif symbols == '-':
        answer = operator.sub(num1, num2)
    elif symbols == '*':
        answer = operator.mul(num1, num2)
    return question, str(answer)
