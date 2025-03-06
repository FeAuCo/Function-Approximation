import visual
from sympy import *


def unexpected_input_func():
    x = symbols('x')

    try:
        test_func = eval("".join(visual.settings_entry_func.get().split()))

        if visual.error_function_unexpected_input.winfo_exists():
            visual.error_function_unexpected_input.place_forget()

        return False

    except (NameError, SyntaxError):
        visual.error_point_unexpected_input.place_forget()
        visual.error_n_unexpected_input.place_forget()
        visual.error_point_unexpected_input.place_forget()

        visual.error_function_unexpected_input.pack()
        visual.error_function_unexpected_input.place(x=150, y=225, anchor="center")
        return True


def unexpected_input_point():
    try:
        splitted_input = visual.settings_entry_point.get().split()

        for char in splitted_input:
            if not char.isdigit() and char != "pi" and char != "E" and char not in (' ', '*', '+', '/', '(', ')'):

                visual.error_n_unexpected_input.place_forget()
                visual.error_function_undefined_at_point.place_forget()

                visual.error_point_unexpected_input.pack()
                visual.error_point_unexpected_input.place(x=150, y=225, anchor="center")

                return True

        if visual.error_point_unexpected_input.winfo_exists():
            visual.error_point_unexpected_input.place_forget()

        return False

    except SyntaxError:
        visual.error_n_unexpected_input.place_forget()
        visual.error_function_undefined_at_point.place_forget()

        visual.error_point_unexpected_input.pack()
        visual.error_point_unexpected_input.place(x=150, y=225, anchor="center")
        return True


def unexpected_input_n():
    try:
        if visual.settings_entry_n.get().isdigit() and int(visual.settings_entry_n.get()) > 0:

            if visual.error_n_unexpected_input.winfo_exists():
                visual.error_n_unexpected_input.place_forget()

            return False
        else:
            visual.error_function_undefined_at_point.place_forget()

            visual.error_n_unexpected_input.pack()
            visual.error_n_unexpected_input.place(x=150, y=225, anchor="center")
            return True

    except SyntaxError:
        visual.error_function_undefined_at_point.place_forget()

        visual.error_n_unexpected_input.pack()
        visual.error_n_unexpected_input.place(x=150, y=225, anchor="center")
        return True


def func_is_undefined_at_point():
    try:
        test_func = (lambdify(symbols('x'), "".join(visual.settings_entry_func.get().split()))
                     (float(eval(visual.settings_entry_point.get()))))

        if visual.error_function_undefined_at_point.winfo_exists():
            visual.error_function_undefined_at_point.place_forget()

        return False

    except SyntaxError:
        unexpected_input_func()

    except ZeroDivisionError:
        visual.error_function_undefined_at_point.pack()
        visual.error_function_undefined_at_point.place(x=150, y=225, anchor="center")
        return True
