#-*- coding:utf-8 -*-
'''
Created on 2015年11月22日

@author: sufy
'''
import cgi
form=cgi.FieldStorage()
print('Content-type:text/html\n')
print('<title>Reply Page</title>')
if not 'user' in form:
    print('<h1>who are you?</h1>')
else:
    print('<h1>Hello<i>%s</i>!</h1>'%cgi.escape(form['user'].value))