# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:14:26 2020

@author: Himanshu
"""

import cv2
import numpy as np
import glob

def reading(path): # path will be like 'Dataset/Training/deepfake/*.avi'
    names = glob(path)
    new_height = new_width = 64  # resolution will be resized to 64(ROUGH IDEA)
    new_videos = np.zeros(shape = [len(names),
                                   40, new_height, new_width]) # contains videos 
    for it, name in enumerate(names):
        vidcap = cv2.VideoCapture(name)
        i = j = 0
        while True:
            success,frame = vidcap.read()
            if 0<=i<40:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # will be changed later if req. 
                resize = cv2.resize(frame, (new_width, new_height))
                new_videos[it, j] = resize
                j = j + 1
            elif i >40:
                break
            i = i + 1
    return new_videos