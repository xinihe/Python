# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:54:24 2018

@author: Administrator
"""

import win32com.client
text="启动记事本"
speaker = win32com.client.Dispatch("SAPI.SpVoice")
phrase='启动记事本'
if phrase=='启动记事本':
    speaker.Speak(text)
    os.popen("notepad.exe")