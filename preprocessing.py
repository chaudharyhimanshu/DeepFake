# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:14:26 2020

@author: Himanshu
"""

import cv2
import numpy as np
from glob import glob

def reading(path): # path will be like 'Dataset/Training/deepfake/*.avi'
    names = glob(path)
    fps = []
    new_height = 1080
    new_width =  1920 #Default resolution of the videos in sample.
    new_videos = np.zeros(shape = [len(names),
                                   100, new_height, new_width]) # contains videos 
    for it, name in enumerate(names):
        vidcap = cv2.VideoCapture(name)
        fps.append(int(vidcap.get(cv2.CAP_PROP_FPS)))
        i = j = 0
        while True:
            success,frame = vidcap.read()
            if 0<=i<40:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # will be changed later if req. 
                #resize = cv2.resize(frame, (new_width, new_height)) #
                new_videos[it, j] = frame
                j = j + 1
            elif i >40:
                break
            i = i + 1
        vidcap.release()
    return [new_videos, names, fps]


path = 'Sample/*.mp4'
sample_data, names, fps = reading(path)
original = sample_data[-1]
deepfake = sample_data[0:-1]
deepfake1_diff = original - deepfake[0]


######Saving Output video######
out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'),
                          fps[0], (1920, 1080), 0)
i = 0
while(1):
    if i < 100:
        v = deepfake1_diff[i]
        v = np.array(v, dtype = np.uint8)
        out.write(v)
        i += 1
    

out.release()
