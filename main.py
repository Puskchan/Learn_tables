import random
from tkinter import *

root = Tk()
root.title("Learn Tables!")
root.configure(bg="#0F044C")

e = Entry(root, width=37, borderwidth=4)
e.grid(row=1, column=0, columnspan=3, padx=20, pady=15)
e.config(font=20, bg="#6E85B2")


def test_out():
    test_out.ans = 0
    x = random.randint(2, 20)
    y = random.randint(2, 8)
    test_out.ans = str(x * y)
    mylab = Label(text=str(str(x) + " x " + str(y)), width=10)
    mylab.grid(row=0, column=0, columnspan=3, pady=15)
    mylab.configure(font=("Times New Roman", 25, "bold"),background="#787A91")


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clearall():
    e.delete(0, END)


def button_check(number):
    answer = str(e.get())
    e.delete(0, END)
    if answer == test_out.ans:
        e.insert(0, "Correct")
        test_out()
    else:
        e.insert(0, "Try Again")



test_out()

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="#EEEEEE")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="#EEEEEE")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="#EEEEEE")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="#EEEEEE")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="#EEEEEE")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="#EEEEEE")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="#EEEEEE")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="#EEEEEE")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="#EEEEEE")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="#EEEEEE")
button_submit = Button(root, text="Check", padx=40, pady=20, command=lambda: button_check(e.get()), bg="#EEEEEE")
button_clear = Button(root, text="Clear", padx=40, pady=20, command=lambda: button_clearall(), bg="#EEEEEE")

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=0)
button_submit.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

root.mainloop()
