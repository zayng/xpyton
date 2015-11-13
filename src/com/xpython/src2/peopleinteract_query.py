#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
import shelve
fieldnames=('name','age','job','pay')
maxfield = max(len(f) for f in fieldnames )
db  = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:break
    try:
        record=db[key]
    except:
        print('No such key "%s"!'%key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield),'=>',getattr(record,field))