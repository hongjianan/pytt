# -*- coding: utf-8 -*-
'''
Created on 2018年10月19日

@author: Administrator
'''
import json
import Tkinter as tk
import ttk


class Method(object):
    ToJson = u'json格式化'
    Null = u'无'

    def __init__(self):
        self.method = {
            self.ToJson: self.to_json,
            self.Null: self.null
        }
    
    @classmethod
    def values(cls):
        return (cls.ToJson, cls.Null)
    
    @staticmethod
    def to_json(input):
        print('to_json', input)
        obj = json.loads(input)
        return json.dumps(obj, sort_keys=True, indent=4,
                          separators=(',', ': '))

    @staticmethod
    def null(input):
        return input
    
    
class Root(object):
    def __init__(self, title=None, weight=900, height=700):
        self.tk = None
        self.title = title
        self.weight = weight
        self.height = height

    def init(self):
        self.tk = tk.Tk()
        self.tk.title(self.title)
        self.tk.geometry('%sx%s' % (self.weight, self.height))
        
    def run(self):
        self.tk.mainloop()


class Tools(object):

    def __init__(self, root):
        self.method = None
        self.root = root
        self.text = None
        
    def draw(self):
        # 创建一个下拉列表
        self.text = tk.StringVar()
        box = ttk.Combobox(self.root, width=12, textvariable=self.text)
        box['values'] = Method.values()     # 设置下拉列表的值
        box.grid(column=0, row=0)      # 设置其在界面中出现的位置  column代表列   row 代表行
        box.current(0)    # 设置下拉列表默认显示的值，0为 numberChosen['values'] 的下标值
        
    def get_method(self):
        content = self.text.get()
        return content
    

class Click(object):

    def __init__(self, root, tools, content):
        self.root = root
        self.tools = tools
        self.content = content
    
    def cb(self):
        data = self.content.get_input()
        print(self.tools.get_method())
        method = Method().method[self.tools.get_method()]
        output = method(data)
        self.content.set_output(output)
        
    def draw(self):
        button = tk.Button(self.root, text="执行", command=self.cb)
        button.grid(row=0, column=1)


class Content(object):

    BEING = '1.0'
    
    def __init__(self, root):
        self.root = root
        self.input = None
        self.output = None
    
    def draw(self):
        self.input = tk.Text(self.root, font=('consolas', 19))
        self.output = tk.Text(self.root, font=('consolas', 19))

        self.input.grid(row=1, column=0)
        self.output.grid(row=2, column=0)
    
    def get_input(self):
        return self.input.get(self.BEING, tk.END)
    
    def set_output(self, data):
        self.output.delete(self.BEING, tk.END)
        return self.output.insert(self.BEING, data)
    
    def copy_output(self):
        return 

    def clear_input(self):
        return self.input.delete(self.BEING, tk.END)


def main():
    root = Root('工具集')
    root.init()
    
    tools = Tools(root.tk)
    content = Content(root.tk)
    click = Click(root.tk, tools, content)
    
    tools.draw()
    content.draw()
    click.draw()

    root.run()


if __name__ == '__main__':
    main()
