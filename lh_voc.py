# # -*- coding: utf-8 -*-
# """
# Created on 18/11/12
#
# @author: zcc
# """
# from skimage import io
# import shutil
# import random
# import os
# import string
# headstr = """\
# <annotation>
#     <folder>VOC2007</folder>
#     <filename>%s</filename>
#     <source>
#         <database>My Database</database>
#         <annotation>PASCAL VOC2007</annotation>
#         <image>flickr</image>
#         <flickrid>NULL</flickrid>
#     </source>
#     <owner>
#         <flickrid>NULL</flickrid>
#         <name>company</name>
#     </owner>
#     <size>
#         <width>%d</width>
#         <height>%d</height>
#         <depth>%d</depth>
#     </size>
#     <segmented>0</segmented>
# """
# objstr = """\
#     <object>
#         <name>%s</name>
#         <pose>Unspecified</pose>
#         <truncated>0</truncated>
#         <difficult>0</difficult>
#         <bndbox>
#             <xmin>%d</xmin>
#             <ymin>%d</ymin>
#             <xmax>%d</xmax>
#             <ymax>%d</ymax>
#         </bndbox>
#     </object>
# """
#
# tailstr = '''\
# </annotation>
# '''
#
# def all_path(filename):
#     return os.path.join('./', filename)
#
# def writexml(name, head, bbxes, tail):
#     filename = all_path("Annotations/%s.xml" % (name.split('.')[0]))
#     f = open(filename, "w")
#     f.write(head)
#     f.write(objstr % ('trueface', bbxes[0], bbxes[1],bbxes[2],bbxes[3]))
#     f.write(tail)
#     f.close()
#
#
# def clear_dir():
#     if shutil.os.path.exists(all_path('Annotations')):
#         shutil.rmtree(all_path('Annotations'))
#     if shutil.os.path.exists(all_path('ImageSets')):
#         shutil.rmtree(all_path('ImageSets'))
#     if shutil.os.path.exists(all_path('JPEGImages')):
#         shutil.rmtree(all_path('JPEGImages'))
#
#     shutil.os.mkdir(all_path('Annotations'))
#     shutil.os.makedirs(all_path('ImageSets/Main'))
#     shutil.os.mkdir(all_path('JPEGImages'))
#
#
# def excute_datasets(datatype):
#     f = open(all_path('ImageSets/Main/' + datatype + '.txt'), 'a')
#     f_bbx = open(all_path('result_true.txt'), 'r')
#
#     for bbox in f_bbx.readlines():
#         bb_info = bbox.split()
#         filename_ = bb_info[0]
#         print(filename_)
#         box = [int(i) for i in bb_info[1:5]]
#         print(box)
#         im = io.imread('E:/ZDHT/raw/trueface/'+filename_)
#         head = headstr % (filename_, im.shape[1], im.shape[0], im.shape[2])
#         writexml(filename_, head, box, tailstr)
#         shutil.copyfile(all_path('E:/ZDHT/raw/trueface/'+filename_), all_path('JPEGImages/%s' % (filename_)))
#         f.write('%s\n' % (filename_))
#     f.close()
#     f_bbx.close()
#
#
# # 打乱样本
# def shuffle_file(filename):
#     f = open(filename, 'r+')
#     lines = f.readlines()
#     random.shuffle(lines)
#     f.seek(0)
#     f.truncate()
#     f.writelines(lines)
#     f.close()
#
#
# if __name__ == '__main__':
#     clear_dir()
#     excute_datasets('train')
#     # idx = excute_datasets(idx, 'val')


# -*- coding: utf-8 -*-
"""
Created on 18/11/12

@author: zcc
"""
from skimage import io
import shutil
import random
import os
from PIL import Image
import string
headstr = """\
<annotation>
    <folder>VOC2007</folder>
    <filename>%s</filename>
    <source>
        <database>My Database</database>
        <annotation>PASCAL VOC2007</annotation>
        <image>flickr</image>
        <flickrid>NULL</flickrid>
    </source>
    <owner>
        <flickrid>NULL</flickrid>
        <name>company</name>
    </owner>
    <size>
        <width>%d</width>
        <height>%d</height>
        <depth>3</depth>
    </size>
    <segmented>0</segmented>
"""
objstr = """\
    <object>
        <name>%s</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
        <bndbox>
            <xmin>%d</xmin>
            <ymin>%d</ymin>
            <xmax>%d</xmax>
            <ymax>%d</ymax>
        </bndbox>
    </object>
"""

tailstr = '''\
</annotation>
'''

def all_path(filename):
    return os.path.join('./', filename)

def writexml(name, head, x1,y1,x2,y2, tail):
    filename = all_path("Annotations/%s.xml" % (name.split('.')[0]))
    f = open(filename, "w")
    f.write(head)
    f.write(objstr % ('face', x1, y1,x2,y2))
    f.write(tail)
    f.close()


def clear_dir():
    if shutil.os.path.exists(all_path('Annotations')):
        shutil.rmtree(all_path('Annotations'))
    if shutil.os.path.exists(all_path('ImageSets')):
        shutil.rmtree(all_path('ImageSets'))
    if shutil.os.path.exists(all_path('JPEGImages')):
        shutil.rmtree(all_path('JPEGImages'))

    shutil.os.mkdir(all_path('Annotations'))
    shutil.os.makedirs(all_path('ImageSets/Main'))
    shutil.os.mkdir(all_path('JPEGImages'))

def retate_handle(count,line):
    f = open(all_path('ImageSets/Main/' + 'train' + '.txt'), 'a')
    bb_info=line.split()
    filename_ = bb_info[0]
    box = [int(i) for i in bb_info[1:5]]
    xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
    im = Image.open('E:/BaiduNetdiskDownload/CelebA/Img/img_celeba.7z/img_celeba/' + filename_)
    w, h = im.size
    #正常图
    if count>=0 and count<1000:
        head = headstr % (filename_, w, h)
        x1 , y1, x2, y2=xmin, ymin, xmax, ymax
        writexml(filename_, head, x1, y1, x2, y2 , tailstr)
        im.save(all_path('JPEGImages/%s' % (filename_)))
    #左转90度
    elif count>=1000 and count<2500:
        im=im.transpose(Image.ROTATE_90)
        head = headstr % (filename_, h, w)
        x1 , y1, x2, y2=ymin, w-xmax, ymax, w-xmin
        writexml(filename_, head, x1, y1, x2, y2 , tailstr)
        im.save(all_path('JPEGImages/%s' % (filename_)))
    #翻转180
    elif count>=2500 and count<4000:
        im=im.transpose(Image.ROTATE_180)
        head = headstr % (filename_, w, h)
        x1 , y1, x2, y2 =w-xmax,h-ymax,w-xmin,h-ymin
        writexml(filename_, head, x1, y1, x2, y2 , tailstr)
        im.save(all_path('JPEGImages/%s' % (filename_)))
    #右转90度
    else:
        im=im.transpose(Image.ROTATE_270)
        head = headstr % (filename_, h, w)
        x1 , y1, x2, y2=h-ymax,xmin,h-ymin,xmax
        writexml(filename_, head, x1, y1, x2, y2 , tailstr)
        im.save(all_path('JPEGImages/%s' % (filename_)))

    f.write('%s\n' % (filename_))
    f.close()

def excute_datasets(datatype):
    f_bbx = open(all_path('./celeba/result_5000.txt'), 'r')
    count=0
    for bbox in f_bbx.readlines():
        retate_handle(count, bbox)
        count+=1

    f_bbx.close()


# 打乱样本
def shuffle_file(filename):
    f = open(filename, 'r+')
    lines = f.readlines()
    random.shuffle(lines)
    f.seek(0)
    f.truncate()
    f.writelines(lines)
    f.close()


if __name__ == '__main__':
    clear_dir()
    excute_datasets('train')
    # idx = excute_datasets(idx, 'val')