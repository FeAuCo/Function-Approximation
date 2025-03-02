import visual
import math


#
# def unexpected_input_func():
#     return True


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
