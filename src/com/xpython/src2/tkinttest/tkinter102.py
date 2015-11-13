#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button = Button(self,text='press',command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='popup', message='Button pressed!')
if __name__=='__main__':
    top=MyGui()
    top.pack()
    top.mainloop()