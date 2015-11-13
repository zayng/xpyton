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
        
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self,percent):
        self.pay*=(1.0+percent)
         
    def __str__(self):
        return '<%s => %s>\n' % (self.__class__.__name__,self.name)
    
if __name__=='__main__':
    bob=Person('Bob Smith',42,30000,'software')
    sue=Person('Sue Jones',45,40000,'hardware')
    
    lastname=bob.lastName()
    print(lastname)
    bob.giveRaise(percent=0.50)
    print(lastname,bob.pay)
#     print(bob.name,bob.pay)
#     print(bob.name.split()[-1])
#     sue.pay*=1.10
#     print(sue.pay)
    