#-*- coding:utf-8 -*-
'''
Created on 2015年10月26日

@author: 119937
'''
import pickle,glob
print(glob.glob('*.pkl'))
for filename in glob.glob('*.pkl'):
    recfile=open(filename,'rb')
    record=pickle.load(recfile)
    print(filename,'=>',record)

suefile=open('sue.pkl','rb')
print(pickle.load(suefile)['name'])
    
