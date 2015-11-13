#-*- coding:utf-8 -*-
'''
Created on 2015年10月21日

@author: 119937
'''
from initdata import db

import pickle

dbfile=open('people-pickle','wb')
pickle.dump(db,dbfile)
dbfile.close()

