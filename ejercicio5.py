import random
import math


def formula(x,y):
    f1 = lambda x, y:  (math.exp(-1*((1/x)-1) * (1+y)) / (x**2)) * ((1/x)-1)
    return f1(x, y)


def evaluate(iter):
    cumu = 0
    for i in range(1, iter):
        rand = random.random()
        rand2 = random.random()
        cumu = cumu + formula(rand, rand2)
    return cumu/iter


def main():
    result = evaluate(1000000)
    print(result)


if __name__ == '__main__':
    main()
