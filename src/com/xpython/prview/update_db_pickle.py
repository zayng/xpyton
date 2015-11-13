#-*- coding:utf-8 -*-
'''
Created on 2015年10月22日

@author: 119937
'''
import pickle
dbfile=('people-pickle','rb')
db=pickle.load(dbfile)
dbfile.close()

db['sue']['pay']*=1.10
db['Tom']['name']='Tom Tom'

dbfile=open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()