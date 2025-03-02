from sympy import *
import math
import error_handler
import visual


def approximate(func, point, n, x):
    if n == 1:
        return f'{lambdify(x, func)(point)} * x / x'

    approximated_func = ''

    for i in range(0, n):
        if i == 0:
            approximated_func += f'({lambdify(x, func)(point)}) + '

        else:
            derivative = diff(eval(str(func)), x, i)

            approximated_func += f'(({lambdify(x, derivative)(point)}) '
            approximated_func += f'* (x - {point}) ** {i}) / {math.factorial(i)} + '

    return Symbol(approximated_func[:-3])


def set_params_and_run():
    if (not error_handler.unexpected_input_point() or not error_handler.unexpected_input_n()):
        func = visual.settings_entry_func.get()
        point = float(visual.settings_entry_point.get())
        n = int(visual.settings_entry_n.get())

        x, y = symbols(f'x {"".join(func.split())}', real=True)

        approximated = lambdify(x, approximate(y, point, n, x))

        graphs = plotting.plot(lambdify(x, func), (x, point - 5, point + 5),
                               ylim=(lambdify(x, func)(point - 5), lambdify(x, func)(point + 5)),
                               show=False)
        graphs.append(plotting.plot(approximated, (x, point - 5, point + 5),
                                    ylim=(lambdify(x, func)(point - 5), lambdify(x, func)(point + 5)),
                                    show=False)[0])

        graphs.show()
