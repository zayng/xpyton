#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')

top=Tk()
quit=Button(top,text='press',command=reply)
quit.pack()
mainloop()