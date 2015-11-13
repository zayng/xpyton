#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
import shelve
from com.xpython.src2.manager import Manager
from com.xpython.src2.person import Person

bob = Person('Bob Smith',42,30000,'software')
sue = Person('Sue Jones',45,40000,'hardware')
tom = Manager('Tom doe',50,50000)

db = shelve.open('class-shelve')
db['bob']=bob
db['sue']=sue
db['tom']=tom

db.close    