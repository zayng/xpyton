#-*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: 119937
'''
from initdata import bob,tom,sue
import shelve
db=shelve.open('people-shelve')
for key in db:
    print(key,'=>\n',db[key])
print(db['sue']['name'])
db.close()
