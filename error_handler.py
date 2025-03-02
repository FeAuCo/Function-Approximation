import visual
from sympy import *


def unexpected_input_func():
    x = symbols('x')

    try:
        test_func = eval("".join(visual.settings_entry_func.get().split()))
        return False
    except (NameError, SyntaxError):
        return True


def unexpected_input_point():
    splitted_input = visual.settings_entry_point.get().split()

    for char in splitted_input:
        if not char.isdigit() and char != "pi" and char != "E" and char not in (' ', '*', '+', '/', '(', ')'):
            return True
    return False


def unexpected_input_n():
    if visual.settings_entry_n.get().isdigit() and int(visual.settings_entry_n.get()) > 0:
        return False
    else:
        return True


def func_is_not_defined_at_point():
    try:
        test_func = (lambdify(symbols('x'), "".join(visual.settings_entry_func.get().split()))
                     (float(eval(visual.settings_entry_point.get()))))
        return False
    except ZeroDivisionError:
        return True
