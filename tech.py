import visual
import error_handler
import approximation


def set_func():
    if (not error_handler.unexpected_input_point() or not error_handler.unexpected_input_n()):
        change_next = False

        with open(file='approximation.py', mode='r') as f:
            lines = f.readlines()
        with open(file='approximation.py', mode='w') as f:
            for line in lines:
                if change_next:
                    f.write(f"    approximated = smp.lambdify(smp.Symbol('x', real=True), "
                            f"approximate(smp.{visual.settings_entry_func.get()}, "
                            f"{int(visual.settings_entry_point.get())}, {int(visual.settings_entry_n.get())}))\n")
                    change_next = False

                elif len(line) > 4 and line[4] == 'x':
                    f.write(f'    x = np.linspace({int(visual.settings_entry_point.get()) - 5}, '
                            f'{int(visual.settings_entry_point.get()) + 5}, 100)\n')

                elif len(line) > 4 and line[4] == 'y':
                    f.write(f'    y = np.{visual.settings_entry_func.get()}(x)\n')

                else:
                    if line.strip("\n") == "    ###":
                        change_next = True
                    f.write(line)



visual.appr_btn['command'] = lambda: (set_func(), approximation.set_params_and_run())

visual.window.mainloop()
