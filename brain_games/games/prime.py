import random

TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def question_and_answer():
    num = random.randint(1, 80)
    answer = 'yes' if is_prime(num) else 'no'
    question = str(num)
    return (question, answer)
