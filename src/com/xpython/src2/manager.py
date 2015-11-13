#-*- coding:utf-8 -*-
'''
Created on 2015年10月31日

@author: 119937
'''
from com.xpython.src2.person import Person

class Manager(Person):
    def giveRaise(self,percent,bount=0.1):
        Person.giveRaise(self, percent+bount)
#         self.pay*=(1.0+percent+bount)
    
if __name__=='__main__':
    tom=Manager(name='Tom Doe',age=50,pay=50000)
    bob=Person('Bob Smith',42,30000,'software')
    sue=Person('Sue Jones',45,40000,'hardware')
    person=[tom,bob,sue]
    for each in person:
        each.giveRaise(0.10)
    for each in person:
        print(each.name,'=>',each.pay)
    print(bob,sue,tom)
#     print(tom.lastName())
#     tom.giveRaise(.20)
#     print(tom.pay)