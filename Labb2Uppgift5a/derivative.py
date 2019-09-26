import math


def derivative(f, x, h):
    return (f(x + h) - f(x - h))/(2 * h)


print(derivative(math.sin, math.pi, 0.0001))
