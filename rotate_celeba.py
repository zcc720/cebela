# '''
# 旋转，以增加左右人脸的泛化性
# '''
#
# import os
# import glob
# import pandas as pd
# import xml.etree.ElementTree as ET
# from PIL import Image
#
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
#         <depth>3</depth>
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
# def read_xml(xml_path):
#     tree = ET.parse(xml_path)
#     root = tree.getroot()
#     for member in root.findall('object'):
#         filename=root.find('filename').text
#         width=int(root.find('size')[0].text)
#         height=int(root.find('size')[1].text)
#         label=member[0].text
#         xmin=int(member[4][0].text)
#         ymin=int(member[4][1].text)
#         xmax=int(member[4][2].text)
#         ymax=int(member[4][3].text)
#         return filename,width,height,label,xmin,ymin,xmax,ymax
#
# def all_path(filename):
#     return os.path.join('./', filename)
#
# def writexml(name, head, x1,y1,x2,y2, tail):
#     filename = all_path("Annotations/%s.xml" % (name.split('.')[0]))
#     f = open(filename, "w")
#     f.write(head)
#     f.write(objstr % ('face', x1, y1,x2,y2))
#     f.write(tail)
#     f.close()
#
# def write_txt(xml_path,type):
#     filename, width, height, label, xmin, ymin, xmax, ymax=read_xml(xml_path)
#     new_xmlpath = all_path("Annotations/%s.xml" % (filename.split('.')[0]))
#     f = open(new_xmlpath, "w")
#     if type==0:
#     #left90
#     if type==1:
#         x1=ymin
#         y1=width-xmax
#         x2=ymax
#         y2=width-xmin
#         w=height
#         h=width
#         label='faceleft'
#     #right90
#     elif type==2:
#         x1 = height-ymax
#         y1 = xmin
#         x2 = height-ymin
#         y2 = xmax
#         w = height
#         h = width
#         label='faceright'
#     #inverted180
#     else:
#         x1=width-xmax
#         y1=height-ymax
#         x2=width-xmin
#         y2=height-ymin
#         w=width
#         h=height
#         label='facedown'
#
#     head = headstr % (filename, w, h)
#     f.write(head)
#     f.write(objstr % (label, x1, y1, x2, y2))
#     f.write(tail)
#     f.close()
#
#
#
#
# def rotate_image(image_path,type,save_dir):
#     im = Image.open(image_path)
#     if type == 1:
#         save_path = save_dir + 'l_'+image_path.split('/')[-1]
#         im = im.transpose(Image.ROTATE_90)
#         im.save(save_path)
#     if type == 2:
#         save_path = save_dir + 'r_'+image_path.split('/')[-1]
#         im = im.transpose(Image.ROTATE_270)
#         im.save(save_path)
#     if type == 3:
#         save_path = save_dir + 'd_'+image_path.split('/')[-1]
#         im = im.transpose(Image.ROTATE_180)
#         im.save(save_path)
#
#
#
#
# if __name__ == '__main__':
#     xmlpath='E:/code/CELEBA/celeba/Annotations/'
#     imgpath='E:/code/CELEBA/celeba/JPEGImages/'
#     image_savedir='E:/code/CELEBA/rotate_celeba_files/JPEGImages/'
#     for i in os.listdir(xmlpath):
#         write_txt(xmlpath+i,1)
#         image_path=imgpath+i.split('.')[0]+'.jpg'
#         rotate_image(image_path,1,image_savedir)



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
    return os.path.join('./rotate_celeba_files/', filename)

def writexml(name, head,x1,y1,x2,y2, tail,type=1):
    if type==1:
        label = 'faceup'
        filename = all_path("up/Annotations/%s.xml" % (name.split('.')[0]))
    elif type==2:
        label = 'faceleft'
        filename = all_path("left/Annotations/%s.xml" % ('l_'+name.split('.')[0]))
    elif type==3:
        label = 'faceright'
        filename = all_path("right/Annotations/%s.xml" % ('r_'+name.split('.')[0]))
    else:
        label = 'facedown'
        filename = all_path("down/Annotations/%s.xml" % ('d_'+name.split('.')[0]))

    f = open(filename, "w")
    f.write(head)
    f.write(objstr % (label, x1, y1,x2,y2))
    f.write(tail)
    f.close()


def clear_dir(type):
    if type==1:
        if shutil.os.path.exists(all_path('up/Annotations')):
            shutil.rmtree(all_path('up/Annotations'))
        if shutil.os.path.exists(all_path('up/JPEGImages')):
            shutil.rmtree(all_path('up/JPEGImages'))
        shutil.os.makedirs(all_path('up/Annotations'))
        shutil.os.makedirs(all_path('up/JPEGImages'))
    if type==2:
        if shutil.os.path.exists(all_path('left/Annotations')):
            shutil.rmtree(all_path('left/Annotations'))
        if shutil.os.path.exists(all_path('left/JPEGImages')):
            shutil.rmtree(all_path('left/JPEGImages'))
        shutil.os.makedirs(all_path('left/Annotations'))
        shutil.os.makedirs(all_path('left/JPEGImages'))
    if type==3:
        if shutil.os.path.exists(all_path('right/Annotations')):
            shutil.rmtree(all_path('right/Annotations'))
        if shutil.os.path.exists(all_path('right/JPEGImages')):
            shutil.rmtree(all_path('right/JPEGImages'))
        shutil.os.makedirs(all_path('right/Annotations'))
        shutil.os.makedirs(all_path('right/JPEGImages'))
    if type==4:
        if shutil.os.path.exists(all_path('down/Annotations')):
            shutil.rmtree(all_path('down/Annotations'))
        if shutil.os.path.exists(all_path('down/Annotations')):
            shutil.rmtree(all_path('down/Annotations'))
        shutil.os.makedirs(all_path('down/Annotations'))
        shutil.os.makedirs(all_path('down/JPEGImages'))


def retate_handle(line,type):
    bb_info=line.split()
    filename_ = bb_info[0]
    box = [int(i) for i in bb_info[1:5]]
    xmin, ymin, xmax, ymax = box[0], box[1], box[2], box[3]
    im = Image.open('E:/BaiduNetdiskDownload/CelebA/Img/img_celeba.7z/img_celeba/' + filename_)
    w, h = im.size
    #正常图
    if type==1:
        head = headstr % (filename_, w, h)
        x1 , y1, x2, y2=xmin, ymin, xmax, ymax
        writexml(filename_, head, x1, y1, x2, y2 , tailstr,type=type)
        im.save(all_path('up/JPEGImages/%s' % (filename_)))
    #左转90度
    elif type==2:
        im=im.transpose(Image.ROTATE_90)
        head = headstr % ('l_'+filename_, h, w)
        x1 , y1, x2, y2=ymin, w-xmax, ymax, w-xmin
        writexml(filename_, head,x1, y1, x2, y2 , tailstr,type=type)
        im.save(all_path('left/JPEGImages/%s' % ('l_'+filename_)))
    # 右转90度
    elif type==3:
        im = im.transpose(Image.ROTATE_270)
        head = headstr % ('r_'+filename_, h, w)
        x1, y1, x2, y2 = h - ymax, xmin, h - ymin, xmax
        writexml(filename_, head, x1, y1, x2, y2, tailstr,type=type)
        im.save(all_path('right/JPEGImages/%s' % ('r_' + filename_)))
    # 翻转180
    else:
        im = im.transpose(Image.ROTATE_180)
        head = headstr % (filename_, w, h)
        x1, y1, x2, y2 = w - xmax, h - ymax, w - xmin, h - ymin
        writexml(filename_, head, x1, y1, x2, y2, tailstr,type=type)
        im.save(all_path('down/JPEGImages/%s' % ('d_' + filename_)))

def excute_datasets(type):
    f_bbx = open('./celeba/result_5000.txt', 'r')
    for bbox in f_bbx.readlines():
        retate_handle(bbox,type)
    f_bbx.close()


if __name__ == '__main__':
    for t in [3,2]:
        clear_dir(type=t)
        excute_datasets(type=t)