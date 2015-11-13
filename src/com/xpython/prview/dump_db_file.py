#-*- coding:utf-8 -*-
'''
Created on 2015年10月6日

@author: 119937
'''
from make_db_file import loadDbase

db = loadDbase()

for key in db:
    print(key,'=>\n ',db[key])
print(db['sue']['name'])