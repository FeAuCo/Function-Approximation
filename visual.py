import tkinter as tk

window = tk.Tk()

window.title("Function Approximation")
window.resizable(False, False)
window.config(bg="#d2d4d3")
window.iconphoto(False, tk.PhotoImage(file='pics/tk_icon.png'))
window.minsize(300, 200)

settings_label = tk.Label(window, text="Settings:", bg="#CFCFCF", relief=tk.RAISED)
settings_entry_func_lable = tk.Label(window, text="Enter your function:", bg="#CFCFCF", relief=tk.FLAT)
settings_entry_point_lable = tk.Label(window, text="Enter point:", bg="#CFCFCF", relief=tk.FLAT)
settings_entry_n_lable = tk.Label(window, text="Enter the ascent:", bg="#CFCFCF", relief=tk.FLAT)

appr_btn = tk.Button(window, text="Approximate:", bg="#d2d4d3", activebackground="#d2d4d3")

settings_entry_func: tk.Entry = tk.Entry(window, bg="#d2d4d3", width=20, state='normal')
settings_entry_point: tk.Entry = tk.Entry(window, bg="#d2d4d3", width=4, state='normal')
settings_entry_n: tk.Entry = tk.Entry(window, bg="#d2d4d3", width=3, state='normal')

appr_btn.pack()

settings_entry_func.pack()
settings_entry_point.pack()
settings_entry_n.pack()

settings_label.pack()
settings_entry_func_lable.pack()
settings_entry_point_lable.pack()
settings_entry_n_lable.pack()

appr_btn.place(x=150, y=185, anchor="center")

settings_entry_func.place(x=150, y=55, anchor="center")
settings_entry_point.place(x=150, y=105, anchor="center")
settings_entry_n.place(x=150, y=155, anchor="center")

settings_entry_func_lable.place(x=150, y=30, anchor="center")
settings_entry_point_lable.place(x=150, y=80, anchor="center")
settings_entry_n_lable.place(x=150, y=130, anchor="center")
