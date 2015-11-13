#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
import shelve
from com.xpython.src2.person import Person
fieldnames=('name','age','job','pay')
maxfield = max(len(f) for f in fieldnames )
db  = shelve.open('class-shelve')

while True:
    key = input('\nKey? => ')
    if not key:break
    if key in db:
        record=db[key]
    else:
        record=Person(name='?',age='?')
    for field in fieldnames:
        currvl=getattr(record, field)
        nextnew=input('\t[%s]=%s\n\t\tnew?=>'%(field,currvl))
        if nextnew:
            setattr(record, field, eval(nextnew))
    db[key]=record
db.close()
        