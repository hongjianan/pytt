# -*- coding: utf-8 -*-

import Tkinter


def gui():
    root = Tkinter.Tk()
    # title
    root.title('工具')
    # size
    root.geometry('600x700')
    # stable 宽不可变, 高可变,默认为True
    # root.resizable(width=False, height=True)
    
    listbox = Tkinter.Listbox(root)
    listbox.geometry('600x700')

    label = Tkinter.Label(root, text = "Hello World.")
    button = Tkinter.Button(root, text = "quit", command = root.quit, bg = "red", fg = "white")
    
    listbox.pack()
    label.pack()
    button.pack(fill = Tkinter.X, expand = 1)
    Tkinter.mainloop()


def run():
    gui()


if __name__ == "__main__":
    run()
    

