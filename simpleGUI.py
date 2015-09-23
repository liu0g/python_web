#encoding=utf-8
__author__ = 'lg'

from tkinter import *  #需要安装Tkinter包  sudo apt-get install python3-tk
import tkinter.messagebox as messagebox

# 在GUI中，每个Button、Label、输入框等，都是一个Widget  Frame是所有Widget的父容器
class Application(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.pack()  #pack()方法把Widget加入到父容器中
        #  pack()是最简单的布局，grid()可以实现复杂的布局
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello,%s'%name)

app = Application()
app.master.title('Hello world')
app.mainloop()
