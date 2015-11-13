#-*- coding:utf-8 -*-
'''
Created on 2015年10月30日

@author: 119937
'''
class Person():
    """
    person类的替代类实现，包含数据，行为和运算符号重载
    """
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
        return '<%s => %s:%s,%s>' % (self.__class__.__name__,self.name,self.job,self.pay)
class Manager(Person):
    """
            带有自定义加薪的person
            继承了通用的lastname,str
    """
    def __init__(self,name,age,pay):
        Person.__init__(self, name, age, pay, job='Manager')
    def giveRaise(self, percent,bouns=0.1):
        Person.giveRaise(self, percent+bouns)
        
if __name__=='__main__':
    bob=Person('Bob Smith',42)
    sue=Person('Sue Jones',45,40000,'hardware')
    tom=Manager(name='Tom doe',age=50,pay=50000)
    
    print(sue,sue.pay,sue.lastName())
    for obj in (bob,sue,tom):
        obj.giveRaise(0.1)
        print(obj)
#     lastname=bob.lastName()
#     print(lastname)
#     bob.giveRaise(percent=0.50)
#     print(lastname,bob.pay)
#     print(bob.name,bob.pay)
#     print(bob.name.split()[-1])
#     sue.pay*=1.10
#     print(sue.pay)
    