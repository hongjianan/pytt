# -*- coding: utf-8 -*-

from Tkinter import *
import ttk


def gui():
    root = Tk()
    # title
    root.title('工具')
    # size
    root.geometry('600x700')
    # stable 宽不可变, 高可变,默认为True
    # root.resizable(width=False, height=True)
    
    listbox = Listbox(root)
    listbox.geometry('600x700')

    label = Label(root, text = "Hello World.")
    button = Button(root, text = "quit", command = root.quit, bg = "red", fg = "white")
    
    listbox.pack()
    label.pack()
    button.pack(fill = X, expand = 1)
    mainloop()


class Writer(object):
    
    def __init__(self, text):
        self.text = text
        self.count = 0
        
    def write(self):
        self.text.insert(END, 'write count: %d\n' % self.count)
        self.count += 1


def text_tt():
    root = Tk()
    root.title("hello world")
    root.geometry('300x200')
    
    text = Text(root)
    
    writer = Writer(text)
    button = Button(root, text="确认", command=writer.write, bg = "red", fg = "white")
    
    button.pack()
    text.pack()
    
    root.mainloop()
    

def listbox_tt():
    root = Tk()
    root.title("hello world")
    root.geometry()
    
    def print_item(event):
        print(lb.get(lb.curselection()))
        
    var = StringVar()
    lb = Listbox(root, listvariable = var)
    list_item = [1, 2, 3, 4]         #控件的内容为1 2 3 4
    for item in list_item:
        lb.insert(END, item)
    lb.delete(2, 4)                  #此时控件的内容为1 3
    
    var.set(('a', 'ab', 'c', 'd'))   #重新设置了，这时控件的内容就编程var的内容了
    print(var.get())
    lb.bind('<ButtonRelease-1>', print_item)
    lb.pack()
        
    root.mainloop()
    

def combobox_tt():
 
    root = Tk()
    root.title("Python GUI")    # 添加标题
    
    Label(root, text="Enter a name").grid(row=0, column=0)      # 设置其在界面中出现的位置  column代表列   row 代表行
    Label(root, text="Chooes a number").grid(row=0, column=1)    # 添加一个标签，并将其列设置为1，行设置为0
    
    # 文本框
    name = StringVar()     # StringVar是Tk库内部定义的字符串变量类型，在这里用于管理部件上面的字符；不过一般用在按钮button上。改变StringVar，按钮上的文字也随之改变。
    nameEntered = Entry(root, width=12, textvariable=name)   # 创建一个文本框，定义长度为12个字符长度，并且将文本框中的内容绑定到上一句定义的name变量上，方便clickMe调用
    nameEntered.grid(column=0, row=1)       # 设置其在界面中出现的位置  column代表列   row 代表行
    nameEntered.focus()     # 当程序运行时,光标默认会出现在该文本框中
     
    # 创建一个下拉列表
    number = StringVar()
    numberChosen = ttk.Combobox(root, width=12, textvariable=number)
    numberChosen['values'] = (1, 2, 4, 42, 100)     # 设置下拉列表的值
    numberChosen.grid(column=1, row=1)      # 设置其在界面中出现的位置  column代表列   row 代表行
    numberChosen.current(1)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
    
    # button被点击之后会被执行
    def click():   # 当acction被点击时,该函数则生效
        action.configure(text='Hello ' + name.get())     # 设置button显示的内容
        action.configure(state='disabled')      # 将按钮设置为灰色状态，不可使用状态
     
    # 按钮
    action = Button(root, text="Click", command=click)     # 创建一个按钮, text：显示按钮上面显示的文字, command：当这个按钮被点击之后会调用command函数
    action.grid(column=2, row=1)    # 设置其在界面中出现的位置  column代表列   row 代表行
    
    root.mainloop()      # 当调用mainloop()时,窗口才会显示出来



if __name__ == "__main__":
#     text_tt()
#     listbox_tt()
    combobox_tt()
