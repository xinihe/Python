# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:12:50 2018

@author: Administrator
"""

import poplib  
import sys  
import smtplib  
from email.mime.text import MIMEText  
import os  
from email.header import decode_header  
import email  
import time  
def check_email():  
    try:          
        p = poplib.POP3('pop3.163.com')  
        p.user('qiao_882@163.com')  
        p.pass_('wff13738024296')  
        ret = p.stat()  
    except:  
        print('Login failed!')  
        sys.exit(1)  
    str = p.top(ret[0], 0) 
    
    strlist = []  
    for x in str[1]:  
        try:  
            strlist.append(x.decode())  
        except:  
            try:  
                strlist.append(x.decode('gbk'))  
            except:  
                strlist.append((x.decode('big5')))  
        mm = email.message_from_string('\n'.join(strlist))  
        print('mm==',mm)
        sub = decode_header(mm['subject'])  
        if sub[0][1]:  
            submsg = sub[0][0].decode(sub[0][1])  
        else:  
            submsg = sub[0][0]  
        if submsg.strip() == '关机':  
            return 0 
        elif submsg.strip() == '重启':  
            return 1 
        p.quit()  
def send_email():  
    user = '20746470@qq.com' 
    pwd = 'wff@13738024296' 
    to = ['qiao_882@163.com', '13738024296@139.com']  #139邮件会有短信提醒,让我知道是否成功  
    msg = MIMEText('')  
    msg['Subject'] = '已收到命令!' 
    msg['From'] = user  
    msg['To'] = ','.join(to)  
    s = smtplib.SMTP('smtp.qq.com')  
    s.login(user, pwd)  
    s.sendmail(user, to, msg.as_string())  
    s.close()  
   
if __name__ == '__main__':  
    while True:  
        time.sleep(20)  
        if check_email() == 0:  
            send_email()  
            os.system('notepad') #关机  
            break 
        if check_email() == 1:  
            send_email()  
            os.system('notepad')  #重启  
            break