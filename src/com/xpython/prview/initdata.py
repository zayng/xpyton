#-*- coding:utf-8 -*-
'''
Created on 2015年10月5日

@author: 119937
'''
#初始化将存储文件、picke和shelve的数据

#记录
bob={'name':'Bob Smith','age':42,'pay':30000,'job':'dev'}
sue={'name':'Sue Jones','age':45,'pay':40000,'job':'hdw'}
tom={'name':'Tom','age':50,'pay':0,'job':None}

#数据库
db={}
db['bob']=bob
db['sue']=sue
db['tom']=tom

if __name__=='__main__':   #做为脚本运行
    for key in db:
        print(key,'=>\n',db[key])