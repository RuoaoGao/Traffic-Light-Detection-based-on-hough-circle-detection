# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 20:59:19 2022

@author: lenovo
"""

import cv2
img = cv2.imread('frames184.jpg')
width = img.shape[0]
height = img.shape[1]
size = (height, width)
print(size)

videoname = "result_green.mp4"  # 要创建的视频文件名称 
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', 'V') # 编码器 
#fourcc = cv2.VideoWriter_fourcc(*'H264')
fps = 200 # 帧率

# 1.要创建的视频文件名称 2.编码器 3.帧率 4.size
videoWrite = cv2.VideoWriter(videoname, fourcc, fps, size)
for i in range(463):
  filename = 'D:/final task/traffic light detection/result/'+'result' + str(i) + '.jpg'
  img = cv2.imread(filename)
  videoWrite.write(img) # 写入
  
videoWrite.release()
