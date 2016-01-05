#-*- coding:utf-8 -*-
'''
Created on 2015年11月23日

@author: 119937
'''
'''
实现用来查看和更新保存在shelve中类实例的基于web的界面；
shelve保存在服务器上（如果是在本地机器，就是同一个机器）
'''
import cgi,shelve,sys,os
shelvename='class-shelve'
fieldnames=('name','age','job','pay')

form = cgi.FieldStorage()
print('Content-type:text/html')
sys.path.insert(0,os.getcwd())

#主html
replyhtml="""
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROW$
    </table>
<p>
    <input type=submit value="Fetch",name=action>
    <input type=submit value="Update",name=action>
</form>
</body></html>

"""
#为$ROW$的数据行html

rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml=''

for fieldname in fieldnames:
    rowshtml+=(rowhtml%((fieldname,)*3))
replyhtml=replyhtml.replace('$ROW$', rowshtml)

def htmlize(adict):
    new=adict.copy()
    for field in fieldnames:
        value=new[field]
        new[field]=cgi.escape(repr(value))
    return new

def fetchRecord(db,form):
    try:
        key=form['key'].value
        record=db[key]
        fields=record.__dict__
        fields['key']=key
    except:
        fields=dict.fromkeys(fieldnames, '?')
        fields['key']='Missing or invalid key!'
    return fields

def updateRecord(db,form):
    if not 'key' in form:
        fields =dict.fromkeys(fieldnames,'?')
        fields['key']='Missing key input!'
    else:
        key=form['key'].value
        if key in db:
            record = db[key]
        else:
            from com.xpython.src2.person import Person
            record=Person(name='?',age='?')
        for field in fieldnames:
            setattr(record,field,eval(form[field].value))
        db[key]=record
        fields=record.__dict__
        fields['key']=key
    return fields
db=shelve.open(shelvename)
action=form['acton'].value if 'action' in form else None
if action=='Fech':
    fields=fetchRecord(db,form)
elif action=='Update':
    fields=updateRecord(db, form)
else:
    fields=dict.fromkeys(fieldnames,'?')
    fields['key']='Miss or invaild action'
db.close()
print(replyhtml%htmlize(fields))