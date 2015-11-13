#-*- coding:utf-8 -*-
'''
Created on 2015年10月30日

@author: 119937
'''
from  initdata import tom
import shelve
db=shelve.open('people-shelve')
sue=db['sue']
sue['pay']*=1.5
db['sue']=sue
db['tom']=tom
db.close() 