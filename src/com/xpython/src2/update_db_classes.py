#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
import shelve

db = shelve.open('class-shelve')
sue=db['sue']
sue.giveRaise(0.25)
db['sue']=sue

tom = db['tom']
tom.giveRaise(0.2)
db['tom'] = tom
db.close()