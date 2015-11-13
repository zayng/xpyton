#-*- coding:utf-8 -*-
'''
Created on 2015年10月22日

@author: 119937
'''
import  pickle
dbfile = open('people-pickle','rb')
db=pickle.load(dbfile)
for key in db:
    print(key,'=>',db[key])
print(db['sue']['name'])