#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from tkinter import *
from com.xpython.src2.tkinttest.tkinter102 import MyGui

mainWin=Tk()
Label(mainWin,text=__name__).pack()

popup=Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainWin.mainloop()