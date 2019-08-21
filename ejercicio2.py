import random
import matplotlib.pyplot as plt


class Fern:

    def point_choice(self, functions, probs):
        selection = []
        for funct, prob in zip(functions,probs):
            selection += [funct] * int(prob * 100)
        return random.choice(selection)

    def functions(self, x, y):
        f1 = lambda x, y: (x * 0.85 + y * 0.04 + 0.0, x * -0.04 + y * 0.85 + 1.6)
        f2 = lambda x, y: (-0.15*x + 0.28*y + 0.0, x*0.26 + y*0.24 + 0.44)
        f3 = lambda x, y: (x*0.2 + y*-0.26 + 0.0, x*0.23 + y*0.22 + 1.6)
        f4 = lambda x, y: (x*0.0 + y*0.0, x*0.0 + y*0.16)
        return [f1(x, y), f2(x, y), f3(x, y), f4(x, y)]

    def paint(self, probs, n=100000):
        pos_x = []
        pos_y = []

        pos_x.append(0)
        pos_y.append(0)

        for i in range(1,n):
            function = self.functions(pos_x[i-1], pos_y[i-1])
            result = self.point_choice(function, probs)
            pos_x.append(result[0])
            pos_y.append(result[1])
        return pos_x, pos_y


def main():
    fern = Fern()
    probabilities = [0.85, 0.07, 0.07, 0.01]
    elections = fern.paint(probabilities)
    plt.plot(elections[0], elections[1], ".")
    plt.show()


if __name__ == "__main__":
    main()


