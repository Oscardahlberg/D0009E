import math


def f1(x):
    return x**2 - 1


def f2(x):
    return math.sin(x)


def f3(x):
    return -x**2 + x + 3


def derivative(f, x, h):
    return (f(x + h) - f(x - h))/(2 * h)


def solve(f, x0, h):
    x = 0
    while True:
        x = x0 - (f(x0)/derivative(f, x0, h))
        if abs(x - x0) < h:
            break
        x0 = x
    return x


print(derivative(f3, 1, 0.0001))
print(solve(f3, 1, 0.0001))
