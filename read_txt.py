import xml.etree.cElementTree as ET
import cv2

# 使用000002.xml作为模板，因为它只有一个object元素
template_file = 'VOC2007/Annotations/000002.xml'
# 生成的xml文件保存的路径
target_dir = 'VOC2007/Annotations/'
# 所有图片的路径
image_dir = 'VOC2007/JPEGImages/'
# 给出所有标注信息的文件，由CelebA提供
bbox_file = 'list_bbox_celeba.txt'
# 图片数量
image_num = 1000

bboxes = open(bbox_file, 'r')

for bbox in bboxes.readlines()[2 : image_num + 2]:
    bb_info = bbox.split()
    image_file = bb_info[0]
    x_1 = int(bb_info[1])
    print('x_1',x_1)
    y_1 = int(bb_info[2])
    print('y_1',y_1)
    width = int(bb_info[3])
    print('width',width)
    height = int(bb_info[4])
    print('height',height)

    im = cv2.imread(image_dir + image_file,1)
    im_width = str(im.shape[0])
    im_height= str(im.shape[1])
    im_depth = str(im.shape[2])



bboxes.close()

print('Done')