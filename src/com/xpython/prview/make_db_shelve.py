#-*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: 119937
'''
from initdata import bob,tom,sue
import shelve
db=shelve.open('people-shelve')
db['bob']=bob
db['sue']=sue
db.close()
