# -*- coding: utf-8 -*-
"""
Created on Thu May 10 09:52:56 2018

@author: Administrator
"""

def ft():
    def flocal():
        u='local u'
        print('in flocal:',u)
    def fnonlocal():
        nonlocal u
        u='nonlocal u'
        print('in fnonlocal:',u)
    def fglobal():
        global u
        u='global u'
        print('in fglobal:',u)
    u='test u'
    flocal()
    print('After local:',u)
   
    fglobal()
    print('After global:',u)
    fnonlocal()
    print('After nonlocal:',u)
    
ft()
print('global var:',u)