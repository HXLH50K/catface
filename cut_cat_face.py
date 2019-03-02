# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:57:54 2019

@author: 25806
"""
import read_dir_files
import cv2
import os
from PIL import Image,ImageDraw

def DetectFaces(image_path):
    cascade_path = "./cascade/haarcascade_frontalcatface.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)

    img = cv2.imread(image_path)
    print(image_path)
    print(type(img))
    if img is None:
        return
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor= 1.02,
                minNeighbors=5,
                minSize=(120, 120),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
    
    result = []
    for (x,y,w,h) in faces:
        result.append((x,y,x+w,y+h))
    
    print("Found {0} faces!".format(len(faces)))
    return result    
      
def SaveFaces(image_path,cnt):
    faces = DetectFaces(image_path)
#    save_dir = image_path.split(".")[1].split("/")[-1]+"_faces"
    if faces:
        #将人脸保存在save_dir目录下。
        #Image模块：Image.open获取图像句柄，crop剪切图像(剪切的区域就是detectFaces返回的坐标)，save保存。
        save_dir = "./source/cut_face"
        if not os.path.exists(save_dir):
            try:
                os.mkdir(save_dir)
            except OSError:
                pass
        
        for (x1,y1,x2,y2) in faces:
            fileName = os.path.join(save_dir,str(cnt)+".jpg")
            Image.open(image_path).crop((x1,y1,x2,y2)).convert("RGB").save(fileName)
            
if __name__ == "__main__":
    dirPath = "./dataset/dogs-vs-cats-redux-kernels-edition/train/dog"
    cnt=0
    fileList = read_dir_files.readDir(dirPath)
    for f in fileList:
#        print (f.split(".")[1].split("/")[-1])
        SaveFaces(f,cnt)
        cnt+=1
    