# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 10:55:49 2022

@author: lenovo
"""

import cv2
from datetime import datetime


def video_to_frames(path):
    """
    输入：path(视频文件的路径)
    """
    # VideoCapture视频读取类
    videoCapture = cv2.VideoCapture()
    videoCapture.open(path)
    # 帧率
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    # 总帧数
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))

    for i in range(int(frames)):
        ret, frame = videoCapture.read()
        cv2.imwrite("D:/final task/traffic light detection/pic/frames%d.jpg" % (i), frame)
    return


if __name__ == '__main__':
    t1 = datetime.now()
    video_to_frames("D:/final task/traffic light detection/CameraSensor_1.avi")
    t2 = datetime.now()
    print("Time cost = ", (t2 - t1))
    print("SUCCEED !!!")

    
    