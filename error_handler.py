import visual
from sympy import *


def unexpected_input_func():
    x = symbols('x')

    try:
        eval("".join(visual.settings_entry_func.get().split()))

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
        cleared_entry = visual.settings_entry_point.get().replace('*', ' ')
        cleared_entry.replace('+', ' ')
        cleared_entry.replace('/', ' ')
        cleared_entry.replace('(', ' ')
        cleared_entry.replace(')', ' ')

        splitted_input = cleared_entry.split()

        for char in splitted_input:
            if (not is_str_float(char)
                    and char != "pi" and char != "E" and char not in (' ', '*', '+', '/', '(', ')')):

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
        (lambdify(symbols('x'), "".join(visual.settings_entry_func.get().split()))
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


def is_str_float(numeric_string):
    try:
        float(numeric_string)

        return True

    except ValueError:
        return False
