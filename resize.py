# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 13:11:35 2019

@author: 25806
"""
import cv2
import read_dir_files
import os
import random

def Resize(img, f):
    #pos 30* neg 40*40
    img = cv2.resize(img, (24, 24), interpolation=cv2.INTER_AREA)
#    img = cv2.resize(img, (40, 40), interpolation=cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Save(f.split("/")[-1], img)

def RandomCut(img, f, cnt):
    a=40
    for i in range(10):
        h = int(random.random() * img.shape[0])
        if h+a>img.shape[0]:
            h=img.shape[0]-a
        w = int(random.random() * img.shape[1])
        if w+a>img.shape[0]:
            w=img.shape[0]-a
        img1 = cv2.cvtColor(img[h:h+a, w:w+a], cv2.COLOR_BGR2GRAY)
        Save(f.split("/")[-1].split(".")[1]+"_"+str(i)+".jpg", img1)
        cnt+=1
    return cnt
    

def Save(img_name, img):
#    save_dir="./source/cut_face/pos_small"
    save_dir="./source/cut_face/neg_small_2"
    if not os.path.exists(save_dir):
        try:
            os.mkdir(save_dir)
        except OSError:
            pass
    
    file_name = save_dir + "/" + img_name
    print(file_name)
    cv2.imwrite(file_name, img)

if __name__ == "__main__":
#    dirPath = "./source/cut_face/pos"
    dirPath = "./dataset/dogs-vs-cats-redux-kernels-edition/train/dog"
    cnt=0
    fileList = read_dir_files.readDir(dirPath)
    for f in fileList:
        img = cv2.imread(f)
        print (f)
        if img is None:
            continue
        else:
#            Resize(img, f)
            cnt = RandomCut(img, f, cnt)
            if cnt >= 10000:
                break
        