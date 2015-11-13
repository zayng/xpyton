#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from tkinter import mainloop
from com.xpython.src2.tkinttest.tkinter102 import MyGui
from tkinter.messagebox import showinfo

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup',message='Ouch')
if __name__=='__main__':
    CustomGui().pack()
    mainloop()