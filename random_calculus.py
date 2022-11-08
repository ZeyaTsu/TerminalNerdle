import sugaku 
import random

calculus = None


def choose():
    ir = random.randint(1, 2)
    global calculus
    sugaku.length = ir
    sugaku.calength = 5
    sugaku.clear()

    calculus = sugaku.oper('with')
    calculus = sugaku.convert(calculus)

    



