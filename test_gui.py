import tkinter as tk

r = tk.Tk()

l = tk.Label(text='press f to make button flash')
l.pack()

b = tk.Button(text='useless button')
b.config(bg='lightgrey')
b.pack()


def flash(event):
    print("f pressed")
    b.config(bg='yellow')
    r.after(2000, lambda: b.config(bg='lightgrey'))


r.bind("<KeyPress-f>", flash)

r.mainloop()
