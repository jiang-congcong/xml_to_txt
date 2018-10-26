import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["kangshifu hong shao noodles","kangshifu suan cai noodles","tea pai","coca cola","pepsi-cola","wahaha yogurt","shu yuan","sha qi ma","da li yuan mian bai","ke bi ke shu pian","kangshifu xiang gu noodles","hao li you","qi du kong jian","haoliyou Q di","ao li ao big cookies","ao li ao small cookies","ABC towel","da li yuan bread","ao li ao qiao xin jie"]  # 自行车检测


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('D://5//xml//%s.xml' % (image_id))

    out_file = open('D://5//txt//%s.txt' % (image_id), 'w')  # 生成txt格式文件
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


#image_ids_train = open('D://5//list.txt').read().strip().split('\',\'')  # 得到所有文件的文件名，读者可以自行写代码得到

# image_ids_val = open('/home/*****/darknet/scripts/VOCdevkit/voc/list').read().strip().split()


list_file_train = open('boat_train.txt', 'w')
list_file_val = open('boat_val.txt', 'w')

#for image_id in image_ids_train:
for image_id in range(1,290):#因为我的图片文件名是从1到289的，所以为了方便，直接用range得到文件名
    list_file_train.write('D://5//jpg//%s.jpg\n' % (image_id))
    convert_annotation(image_id)
list_file_train.close()  # 只生成训练集，自己根据自己情况决定

# for image_id in image_ids_val:

#    list_file_val.write('/home/*****/darknet/boat_detect/images/%s.jpg\n'%(image_id))
#    convert_annotation(image_id)
# list_file_val.close()
