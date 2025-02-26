import visual
import approximation
import numpy as np
import sympy as smp


visual.appr_btn['command'] = lambda: (approximation.set_params_and_run(getattr(np, visual.settings_entry_func.get()),
                                                                       getattr(smp, visual.settings_entry_func.get())))

visual.window.mainloop()
