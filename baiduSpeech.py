# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:31:13 2018

@author: Administrator
"""

from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '10600655'
API_KEY = '6I9lKpPq822YsqeglDQuM1WZ'
SECRET_KEY = 'GIXoDlDgAgwyUYk8KwA6pErOEY3QzbB9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
'''
result=client.synthesis('你好百度','zh',1,{'vol':5})
if not isinstance(result, dict):
    with open(r'd:\bdauido.wav', 'wb') as f:
        f.write(result)
'''
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
resp=client.asr(get_file_content(r'd:\bdauido.wav'), 'wav', 8000, {
    'dev_pid': '1537',
})
print(resp)
