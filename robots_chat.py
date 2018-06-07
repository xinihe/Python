# -*- coding: utf-8 -*-
"""
Created on Mon May 14 09:05:44 2018

@author: Administrator
"""

from time import sleep 
import requests 
#s = input("请主人输入话题：") 

s = "娱乐圈"
while True: 
    resp = requests.post("http://www.tuling123.com/openapi/api",data={"key": "67113a1fce7e47f0b35f0e13aac90fae", "info": s, }) 
    resp = resp.json() 
    sleep(1) 
    print('小鱼：', resp['text']) 
    s = resp['text'] 
    resp = requests.get("http://api.qingyunke.com/api.php", {'key': 'free', 'appid': 0, 'msg': s}) 
    resp.encoding = 'utf8' 
    resp = resp.json() 
    sleep(1) 
    print('菲菲：', resp['content'])
    s = resp['content'] 
    resp = requests.post("http://openapi.tuling123.com/openapi/api/v2",data={"perception": {"inputText": {"text": "附近的酒店"}},"userInfo":{"apiKey":"67113a1fce7e47f0b35f0e13aac90fae","userId":"263370"}}) 
    resp = resp.json() 
    sleep(1) 
    print('小方：', resp) 
   