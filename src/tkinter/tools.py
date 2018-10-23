# -*- coding: utf-8 -*-
'''
Created on 2018年10月19日

@author: Administrator
'''
import json
import traceback
import Tkinter as tk
import ttk

 
class Transformer(object):
    def transform_ex(self, data):
        pass

    def transform(self, data):
        try:
            return self.transform_ex(data)
        except Exception:
            msg = traceback.format_exc()
            return msg


class Json(Transformer):

    def transform_ex(self, data):
        data = data.replace("'", '"')
        obj = json.loads(data)
        return json.dumps(obj, sort_keys=True, indent=4,
                          separators=(',', ': '))
    

class PerlPath(Transformer):
    PERL_PATH = '::'
    LINUX_FILE_PATH = '/'
    WINDOWS_FILE_PATH = '\\'

    def transform_ex(self, data):
        if self.PERL_PATH in data:
            out = data.replace(self.PERL_PATH, self.WINDOWS_FILE_PATH)
        elif self.FILE_PATH in input:
            out = data.replace(self.WINDOWS_FILE_PATH, self.PERL_PATH)
        else:
            out = data
        return out
    

class Method(object):
    # 功能
    ToJson = u'json格式化'
    ToPerlPath = u'perl路径'
    Null = u'无'

    def __init__(self):
        self.method = {
            self.ToJson: self.to_json,
            self.ToPerlPath: self.to_perl_path,
            self.Null: self.null
        }
    
    @classmethod
    def values(cls):
        return (cls.ToJson, cls.ToPerlPath, cls.Null)
    
    @staticmethod
    def to_json(data):
        return Json().transform(data)
    
    @staticmethod
    def to_perl_path(data):
        return PerlPath().transform(data)

    @staticmethod
    def null(data):
        return data
    
    
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
        
    def draw(self, column, row):
        # 创建一个下拉列表
        self.text = tk.StringVar()
        box = ttk.Combobox(self.root, width=12, textvariable=self.text)
        box['values'] = Method.values()     # 设置下拉列表的值
        box.grid(row=row, column=column, sticky='w', padx='300')      # 设置其在界面中出现的位置  column代表列   row 代表行
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
        method = Method().method[self.tools.get_method()]
        output = method(data)
        self.content.set_output(output)
        
    def draw(self, row, column):
        button = tk.Button(self.root, text="执行", command=self.cb)
        button.grid(row=row, column=column, sticky='e', padx='300')


class Content(object):

    BEING = '1.0'
    
    def __init__(self, root):
        self.root = root
        self.input = None
        self.output = None
    
    def draw(self):
        self.input = tk.Text(self.root, font=('consolas', 12), width=98, height=17)
        self.output = tk.Text(self.root, font=('consolas', 12), width=98, height=17)
#         self.input.geometry('%sx%s' % (self.weight, self.height))
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


class QuickKey(object):
    def __init__(self, root, click):
        self.root = root
        self.click = click
    
    def event_handler(self, event):
        if event.keysym == 'F3':
            self.click.cb()

    def register_key(self):
        self.root.bind_all('<KeyPress>', self.event_handler)


def main():
    root = Root('工具集')
    root.init()
    
    tools = Tools(root.tk)
    content = Content(root.tk)
    click = Click(root.tk, tools, content)
    key = QuickKey(root.tk, click)
    
    key.register_key()
    tools.draw(0, 0)
    content.draw()
    click.draw(0, 0)
    
    root.run()


if __name__ == '__main__':
    main()
