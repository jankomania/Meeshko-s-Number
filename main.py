import random
import tkinter as tk


def guess():
    print('guess')


if __name__ == '__main__':
    # Creates 500x500 window
    window = tk.Tk()
    window.title("Mishko's Number")
    window.geometry('500x500')

    # Entry variables
    ifrom = tk.StringVar()
    ito = tk.StringVar()

    # Starting Resources
    gold = tk.StringVar()

    # Creates entries and descriptions
    tk.Label(window, text="Mishko's Number", font=('Ubuntu', 30)).place(x=90, y=60)

    tk.Label(window, text='From:', font='Ubuntu').place(x=50, y=200)
    tk.Entry(window, textvariable=ifrom, width=10).place(x=100, y=200)

    tk.Label(window, text='To:', font='Ubuntu').place(x=320, y=200)
    tk.Entry(window, textvariable=ito, width=10).place(x=350, y=200)

    tk.Button(window, text='Guess', font=('Ubuntu', 15), width=15, height=3, command=guess).place(x=160, y=390)

    # Main Loop
    window.mainloop()
