from tkinter import *
from tkinter import ttk

mainform = Tk()
mainform.title("GUI app test")

# widget
frame1 = ttk.Frame(mainform, padding = 16)
label1 = ttk.Label(frame1, text = "Enter text")
t = StringVar()
entry1 = ttk.Entry(frame1, textvariable = t)
button1 = ttk.Button(frame1, text = "OK", command = lambda:
print("This is %s." % t.get()))

# Layout
frame1.pack()
label1.pack(side = LEFT)
entry1.pack(side = LEFT)
button1.pack(side = LEFT)

mainform.mainloop()
