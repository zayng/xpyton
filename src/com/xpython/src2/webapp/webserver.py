#-*- coding:utf-8 -*-
'''
Created on 2015年11月22日

@author: sufy
'''
import os,sys
from http.server import HTTPServer,CGIHTTPRequestHandler
webdir='.'
port=80
os.chdir(webdir)
srvradd=("",port)
srvrobj=HTTPServer(srvradd,CGIHTTPRequestHandler)
srvrobj.serve_forever()