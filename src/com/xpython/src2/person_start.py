#-*- coding:utf-8 -*-
'''
Created on 2015年10月30日

@author: 119937
'''
class Person():
    def __init__(self,name,age,pay=0,job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
        
if __name__=='__main__':
    bob=Person('Bob Smith',42,30000,'software')
    sue=Person('Sue Jones',45,40000,'hardware')
    
    print(bob.name,bob.pay)
    print(bob.name.split()[-1])
    sue.pay*=1.10
    print(sue.pay)
    