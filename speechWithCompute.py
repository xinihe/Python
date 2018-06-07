# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:40:57 2018

@author: Administrator
"""

import speech
import time

response = speech.input("Say something, please.")
speech.say("You said " + response)

def callback(phrase, listener):
    if phrase == "goodbye":
        listener.stoplistening()
    speech.say(phrase)

listener = speech.listenforanything(callback)
while listener.islistening():
    time.sleep(.5)