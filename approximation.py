import numpy as np
from matplotlib import pyplot as plt
import sympy as smp
import math


def approximate(func, point, n):
    if n == 1:
        return f'{func(point)} * x / x'

    arg = smp.symbols('arg', real=True)
    approximated_func = ''

    for i in range(0, n):
        if i == 0:
            approximated_func += f'({func(point)}) + '

        else:
            derivative = smp.diff(func(arg), (arg, i))

            approximated_func += f'(({derivative.evalf(subs={arg: point})}) '
            approximated_func += f'* (x - {point}) ** {i}) / {math.factorial(i)} + '

    return smp.Symbol(approximated_func[:-3])


def set_params_and_run():
    plt.rcParams["figure.figsize"] = (10, 7)

    fig, ax = plt.subplots()
    x = np.linspace(-4, 4, 100)
    y = np.cos(x)

    ax.grid()
    ax.plot(x, y)
    ###
    approximated = smp.lambdify(smp.Symbol('x', real=True), approximate(smp.cos, 0, 4))

    ax.plot(x, approximated(x), "black")
    plt.show()
