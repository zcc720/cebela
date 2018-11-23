from PIL import Image
import cv2
import matplotlib.pyplot as plt
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
def rotate(image_name,savepath):
    img = Image.open(image_name)
    w, h = img.size
    rotate_img = img.transpose(Image.ROTATE_180)
    # rotate_img.show()
    rotate_img.save(savepath)

image_dir = 'E:/code/Widerface/widerface/d180/JPEGImages/'
save_dir='E:/wider_rotate/d180/JPEGImages/'
for i in os.listdir(image_dir):
    print(i)
    rotate(image_dir+i,save_dir+i)



# # 生成的xml文件保存的路径
# target_dir = './celeba/Annotations/'
# # 所有图片的路径
# image_dir = './celeba/JPEGImages/'
# # 给出所有标注信息的文件，由CelebA提供
# bbox_file = 'list_bbox_celeba.txt'


# # 图片数量
# image_num = 1000
#
# bboxes = open(bbox_file, 'r')
#
# def image_info(line):
#     bb_info = line.split()
#     image_file = bb_info[0]
#     x1 = int(bb_info[1])
#     y1 = int(bb_info[2])
#     x2 = int(bb_info[3])+int(bb_info[1])
#     y2 = int(bb_info[4])+int(bb_info[2])
#     im = cv2.imread(image_dir + image_file)
#     im=cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
#     im_width = int(im.shape[0])
#     # im_height= int(im.shape[1])
#     return x1,y1,x2,y2,im_width,im
#
# for bbox in bboxes.readlines()[2 : image_num + 2]:
#     fig = plt.figure()
#     x1, y1, x2, y2, im_width,im=image_info(bbox)
#     im = cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 3)
#     plt.imshow(im)
#     plt.show()
#
# bboxes.close()