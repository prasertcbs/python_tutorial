import matplotlib.pyplot as plt
import math
import numpy as np


def quadratic(a, b, c):
    # ax^2 + bx + c = 0
    d = b * b - 4 * a * c
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    else:
        return math.nan, math.nan


def vertex(a, b, c):
    x = -b / (2 * a)
    y = (4 * a * c - b ** 2) / (4 * a)
    return x, y


def plot_parabola(a, b, c):
    x1, x2 = quadratic(a, b, c)
    vx, vy = vertex(a, b, c)
    factor = abs(x1 - x2) * .2
    minX = min((x1, x2)) - factor
    maxX = max((x1, x2)) + factor
    x = np.linspace(minX, maxX, 100)
    y = a * x ** 2 + b * x + c
    plt.plot(x, y)
    plt.axhline(y=0, color='r', linestyle='--')
    plt.axvline(x=x1, color='g', linestyle='--')
    plt.axvline(x=x2, color='g', linestyle='--')
    plt.title(f'x1 = {x1}, x2 = {x2}\nvertex = ({vx}, {vy})')
    plt.show()


if __name__ == '__main__':
    # a, b, c = 2, 7, 3
    a, b, c = map(float, input("a b c: ").split(" "))
    x1, x2 = quadratic(a, b, c)
    print(f"x1 = {x1}, x2 = {x2}")
    vx, vy = vertex(a, b, c)
    print(f"vertex = ({vx}, {vy})")
    plot_parabola(a, b, c)
