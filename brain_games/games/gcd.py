import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num2


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    gcd_value = gcd(num1, num2)
    return question, str(gcd_value)
