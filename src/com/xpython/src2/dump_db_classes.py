#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key,'=>',db[key].name,db[key].pay)
    
bob=db['bob']
print(bob.lastName())
