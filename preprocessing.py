# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:14:26 2020

@author: Himanshu
"""

import cv2
import numpy as np
from glob import glob
import os
import matplotlib.pyplot as plt

def sub(img, channel, cat):
    fig = plt.figure(figsize = (20, 10))
    for i in range(len(img)):
        plt.subplot(2, 2, i + 1)
        image = img[i]
        plt.hist(image[:,:,channel].ravel(),256,[0,256]) 
    fig.savefig(cat + str(channel) + '.png')

def plot_img(img, cat):
    fig = plt.figure(figsize = (20, 10))
    for i in range(len(img)):
        plt.subplot(2, 2, i + 1)
        plt.imshow(img[i])
    fig.savefig(cat+'.png')



def reading(names, path): # path will be like 'Dataset/Training/deepfake/*.avi'
    #names = glob(path)
    #fps = []
    #new_height = 1080
    #new_width =  1920 #Default resolution of the videos in sample.
    new_videos = []#np.zeros(shape = [len(names),
                  #                 40, new_height, new_width]) # contains videos 
    for it, name in enumerate(names):
        vidcap = cv2.VideoCapture(path + name)
        #fps.append(int(vidcap.get(cv2.CAP_PROP_FPS)))
        i = 0
        fig = plt.figure(figsize = (20, 10))
        while True:
            success,frame = vidcap.read()
            if 0<=i<40:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # will be changed later if req. 
                #resize = cv2.resize(frame, (new_width, new_height)) #
                #new_videos[it, j] = frame
                plt.subplot(4, 10, i + 1)
                plt.hist(frame.ravel(),256,[0,256]) 
                #new_videos.append(frame)
                #j = j + 1
            elif i >40:
                break
            i = i + 1
        fig.savefig(name + '.png')
        vidcap.release()
    return [new_videos, names]

def hist(names, path):
    for it, name in enumerate(names):
        vidcap = cv2.VideoCapture(path + name)
        i = 0
        fig = plt.figure(figsize = (20, 10))
        while True:
            success,frame = vidcap.read()
            if 0<=i<40:
                frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                plt.subplot(4, 10, i + 1)
                mask = frame == 0
                frame = frame[~mask]
                plt.hist(frame,256,[0,256]) 
            elif i >40:
                break
            i = i + 1
        fig.savefig(name + '.png')
        vidcap.release()



def inconsistency(names, path):
    for name in names:
        vidcap = cv2.VideoCapture(path + name)
        i = 0
        fig = plt.figure(figsize = (20, 10))
        success,frame1 = vidcap.read()
        frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
        while True:
            success,frame2 = vidcap.read()
            if 0<=i<40:
                frame2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
                diff = frame2.astype(int) - frame1.astype(int)
                mask = diff == 0
                diff = diff[~mask]
                plt.subplot(4, 10, i + 1)
                plt.hist(diff,256 * 2 - 1,[-255,256])
                frame1 = frame2
            elif i >41:
                break
            i = i + 1
        fig.savefig(name + '.png')
        vidcap.release()




path = os.getcwd() + '\\Sample\\'
categories = os.listdir(path)
target = []
train = []
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
