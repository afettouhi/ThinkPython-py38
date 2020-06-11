import math


def eval_loop():
    while True:
        i = input("Input: ")
        if i == 'done':
            break
        else:
            print(eval(i))


eval_loop()
