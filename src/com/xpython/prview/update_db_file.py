#-*- coding:utf-8 -*-
'''
Created on 2015年10月6日

@author: 119937
'''
from make_db_file import  storeDbase,loadDbase
db=loadDbase()
db['sue']['pay'] *=1.10
db['tom']['name']='Tom Tom'
storeDbase(db)
