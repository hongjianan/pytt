# coding: UTF-8

import Tkinter


def gui():
    top = Tkinter.Tk()
    label = Tkinter.Label(top, text = "Hello World.")
    button = Tkinter.Button(top, text = "quit", command = top.quit, bg = "red", fg = "white")

    label.pack()
    button.pack(fill = Tkinter.X, expand = 1)
    Tkinter.mainloop()


def run():
    gui()


if __name__ == "__main__":
    run()
    

