# -*- coding: utf-8 -*-
"""
Created on 18/10/30

@author: zcc
"""
from skimage import io
import shutil
import random
import os
import string
image_num=1000
headstr = """\
<annotation>
    <folder>VOC2007</folder>
    <filename>%06d.jpg</filename>
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
        <depth>%d</depth>
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

def writexml(idx, head, bbxes, tail):
    filename = all_path("Annotations/%06d.xml" % (idx))
    f = open(filename, "w")
    f.write(head)
    f.write(objstr % ('face', bbxes[0], bbxes[1],bbxes[0]+bbxes[2],bbxes[1]+bbxes[3]))
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


def excute_datasets(idx, datatype):
    f = open(all_path('ImageSets/Main/' + datatype + '.txt'), 'a')
    f_bbx = open(all_path('list_bbox_celeba.txt'), 'r')

    for bbox in f_bbx.readlines()[2: image_num + 2]:
        bb_info = bbox.split()
        filename_ = bb_info[0]
        print(filename_)
        box = [int(i) for i in bb_info[1:5]]
        print(box)
        im = io.imread('E:/BaiduNetdiskDownload/CelebA/Img/img_celeba.7z/img_celeba/'+filename_)
        head = headstr % (idx, im.shape[1], im.shape[0], im.shape[2])
        writexml(idx, head, box, tailstr)
        shutil.copyfile(all_path('E:/BaiduNetdiskDownload/CelebA/Img/img_celeba.7z/img_celeba/'+filename_), all_path('JPEGImages/%06d.jpg' % (idx)))
        f.write('%06d\n' % (idx))
        idx +=1
    f.close()
    f_bbx.close()
    return idx


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
    idx = 1
    idx = excute_datasets(idx, 'train')
    # idx = excute_datasets(idx, 'val')