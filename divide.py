# -*- coding:utf8 -*-
import json
from os import listdir
import os

path = '/home/flychen/frustum-pointnets-master/dataset/kitti/object/label_2/'
path2='dataset/KITTI/object/training/image_2/'

filelist = listdir(path)
print(filelist)
#for u in  filelist:
# print(filelist[0].split(".")[0])
#   u.split()
fileIndex = []

# 文件名读入时并非按照我们常识中的按照文件名字顺序读入，
# 例如：1.json,2.json,3.json；程序可能会按 3,1,2 的顺序读入，
# 这对我们后面批量处理造成很大的不便，所以读入文件名后，
# 我们要手动地对文件名进行一次排序
# 以下就是排序操作
for i in range(0, len(filelist)):
    index = filelist[i].split(".")[0]
    fileIndex.append(int(index))
# new_filelist =[]
for j in range(1, len(fileIndex)):
    for k in range(0, len(fileIndex) - 1):
        if fileIndex[k] > fileIndex[k + 1]:
            preIndex = fileIndex[k]
            preFile = filelist[k]
            fileIndex[k] = fileIndex[k + 1]
            filelist[k] = filelist[k + 1]
            fileIndex[k + 1] = preIndex
            filelist[k + 1] = preFile
print(filelist)

# 完成排序后，开始按照文件名顺序读取文件内容信息
data = []  # 记录每个文件最终信息的列表

for file in filelist:
    print(file)
    with open(path + file, 'r') as txt:
        lines = txt.readlines()

        eachdata = []  # 记录单个文件信息的列表

        for each in range(len(lines)):

            word = lines[each].split('\n')[0]

            if word[:3] == 'car':
                    eachdata.append(path2)
                    eachdata.append(file.split('.')[0])
                    eachdata.append('.png 1 0.9 ')
                    eachdata.append(word[20:35])
                    eachdata.append('\n')


            if word[:5] == 'truck':
                    eachdata.append(path2)
                    eachdata.append(file.split('.')[0])
                    eachdata.append('.png 2 0.9 ')
                    eachdata.append(word[22:37])
                    eachdata.append('\n')


        txt.close()
        data.append(eachdata)


# 记录完成后，开始将数据写入txt文件
with open('data5.txt', 'w') as txt:
    for eachdata in data:
        line = ''
        for i in range(len(eachdata)):
         s = str(eachdata[i])
         line = line + s

        txt.writelines(line)
    txt.close()


#        line='json'
#        while line:
#           line = txt.readline()
#          word = line.split()
#         for i in range(0,len(word)):

