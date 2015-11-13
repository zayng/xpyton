#-*- coding:utf-8 -*-
'''
Created on 2015年10月5日

@author: 119937
'''
import sys

db_filename='people'
ENDDB='enddb.'
ENDREC='endrec.'
RECSEP='=>'

#将数据储存到文件，需要存储对象db,存储文件默认文件名:people
def storeDbase(db,filename=db_filename):
    dbfile=open(filename,'w')
    for key in db:
        print(key,file=dbfile)
        for (name,value) in db[key].items():
            print(name+RECSEP+repr(value),file=dbfile)
        print(ENDREC,file=dbfile)
    print(ENDDB,file=dbfile)
    dbfile.close()

def loadDbase(dbfilename=db_filename):
    '''读取文件数据，重新构建数据库'''
    db={}
    dbfile=open(dbfilename)
    sys.stdin=dbfile
    key=input()
    while key !=ENDDB:
        rec={}
        filed=input()
        while filed != ENDREC:
            name,value=filed.split(RECSEP)
            rec[name]=eval(value)
            filed=input()
        db[key]=rec
        key=input()
    return db

if __name__=='__main__':
    from initdata import db
    storeDbase(db)
        
        
    
