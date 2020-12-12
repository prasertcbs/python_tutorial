'''
rock paper scissors simulation
'''
import random


def rand_shape():
    d = {"r": "rock", "p": "paper", "s": "scissors"}
#    d = {"r": "\u270a", "p": "\u270b", "s": "\u270c"}
    return random.choice(list(d.values()))


def play(shape1, shape2):
    score = 0
    if shape1 == shape2:
        result = f'{shape1:8} = {shape2}'
    elif (shape1 == "rock" and shape2 == "scissors") \
            or (shape1 == "paper" and shape2 == "rock") \
            or (shape1 == "scissors" and shape2 == "paper"):
        result = f'{shape1:8} > {shape2}'
        score = 1
    else:
        result = f'{shape1:8} < {shape2}'
        score = -1
    return score, result


if __name__ == '__main__':
    total_score = 0
    for i in range(1, 21):
        p1 = rand_shape()
        p2 = rand_shape()
        score, result = play(p1, p2)
        print(f'round:{i:3} {result}')
        total_score = total_score + score
    print(f'total_score = {total_score}')
