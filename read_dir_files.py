# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:08:17 2019

@author: 25806
"""

import os

def readDir(dirPath):
    if dirPath[-1] == '/':
        print ('文件夹路径末尾不能加/')
        return
    allFiles = []
    if os.path.isdir(dirPath):
        fileList = os.listdir(dirPath)
        for f in fileList:
            f = dirPath+'/'+f
            if os.path.isdir(f):
                subFiles = readDir(f)
                allFiles = subFiles + allFiles #合并当前目录与子目录的所有文件路径
            else:
                allFiles.append(f)
        return allFiles
    else:
        return 'Error,not a dir'