#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from tkinter import *
from tkinter.messagebox import showinfo
import shelve

shelvename='class-shelves'
fieldnames=('name','age','job','pay') 

top = Tk()
top.title("People Shelve")

keyLabel=Label(top,text='key\t')
keyLabel.pack(side=LEFT)
keyEnt=Entry(top)
keyEnt.pack(side=RIGHT)
top.mainloop()