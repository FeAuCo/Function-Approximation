import visual

#
# def unexpected_input_func():
#     return True


def unexpected_input_point():
    try:
        if int(visual.settings_entry_point.get()) or int(visual.settings_entry_point.get()) == 0:
            return False
    except ValueError:
        return True


def unexpected_input_n():
    try:
        if int(visual.settings_entry_n.get()) or int(visual.settings_entry_n.get()) == 0:
            return False
    except ValueError:
        return True
