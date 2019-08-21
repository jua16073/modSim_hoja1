import random
import math


def formula(x):
    return math.exp(-((1/x)-1) ** 2)/x ** 2


def evaluate(iter):
    cumu = 0
    for i in range(1, iter):
        rand = random.random()
        cumu = cumu + 2*formula(rand)
    return cumu/iter


def main():
    result = evaluate(1000000)
    print(result)


if __name__ == '__main__':
    main()




