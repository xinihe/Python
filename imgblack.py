# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:02:04 2018

@author: Administrator
"""

import PIL.Image
im = Image.open(r'd:\s.jpg') # 读取图片
im.rotate(45).show() # 将图片旋转，并用系统自带的图片工具显示图片
'''
from PIL import Image
import numpy as np
a=np.asarray(Image.open(r'd:\s.jpg'))

depth=10.
grad=np.gradient(a)#图像灰度的梯度值
grad_x,grad_y=grad
grad_x=grad_x*depth/100.
grad_y=grad_y*depth/100.
A=np.sqrt(grad_x**2+grad_y**2+1.)
uni_x=grad_x/A
uni_y=grad_y/A
uni_z=1./A
vec_el=np.pi/2.2 #光源的俯视角度 弧度值
vec_az=np.pi/4. #光源的方位角度 弧度值
dx=np.cos(vec_el)*np.cos(vec_az)
dy=np.cos(vec_el)*np.sin(vec_az)
dz=np.sin(vec_el)
b=255*(dx*uni_x+dy*uni_y+dz*uni_z)
b=b.clip(0,255)
im=Image.fromarray(b.astype('uint8'))
im.save(r'd:\b.jpg')
'''