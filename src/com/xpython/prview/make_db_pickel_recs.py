#-*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: 119937
'''
from initdata import bob,sue,tom
import pickle
for (key,record) in [('bob',bob),('tom',tom),('sue',sue)]:
    recfile=open(key+'.pkl','wb')
    pickle.dump(record,recfile)
    recfile.close()