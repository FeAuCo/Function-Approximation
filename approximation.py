import numpy as np
from matplotlib import pyplot as plt
import sympy as smp
import math
import error_handler
import visual


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


def set_params_and_run(y_func, approximate_func):
    if (not error_handler.unexpected_input_point() or not error_handler.unexpected_input_n()):
        plt.rcParams["figure.figsize"] = (10, 7)

        fig, ax = plt.subplots()
        x = np.linspace(0, 10, 100)
        y = y_func(x)

        ax.grid()
        ax.plot(x, y)

        approximated = smp.lambdify(smp.Symbol('x', real=True), approximate(approximate_func, 5, 5))

        ax.plot(x, approximated(x), "black")
        plt.show()
