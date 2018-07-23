from random import *
from eval import calc

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(["+", "-", "*", "/"])

    error = choice([-1, 0, 1])

    display_result = calc(x, y, op) + error

    return [x, y, op, display_result]



def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if  calc(x, y, op) == result:
            return True
        else:
            return False
    else: 
        if calc(x, y, op) == result:
            return False
        else:
            return True


