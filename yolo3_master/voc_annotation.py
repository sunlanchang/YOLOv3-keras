import xml.etree.ElementTree as ET
from os import getcwd

sets = [('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

# ****************************自己训练的类别目录******************
# classes = ["airplane", "ship"]
  
classes =   ['aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor']


def convert_annotation(year, image_id, list_file):
    in_file = open('../../data/VOC%stest/Annotations/%s.xml' %
                   (year, image_id))
    tree = ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls_ = obj.find('name').text
        # 训练自己数据
        # if cls_ not in classes or int(difficult) == 1:
        #     continue
        cls_id = classes.index(cls_)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),
             int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a)
                                        for a in b]) + ',' + str(cls_id))


# wd = getcwd()

# for year, image_set in sets:
#     image_ids = open('../../data/VOC%s/ImageSets/Main/%s.txt' %
#                      (year, image_set)).read().strip().split()
#     list_file = open('%s_%s.txt' % (year, image_set), 'w')
#     for image_id in image_ids:
#         list_file.write('%s/../../data/VOC%s/JPEGImages/%s.jpg' %
#                         (wd, year, image_id))
#         convert_annotation(year, image_id, list_file)
#         list_file.write('\n')
#     list_file.close()
# for year, image_set in sets:
year = 2007
# image_set = 'train'
# image_set = 'val'
image_set = 'test'
image_ids = open('../../data/VOC%stest/ImageSets/Main/%s.txt' %
                 (year, image_set)).read().strip().split()
list_file = open('data_anotation_2_txt/%s_%s.txt' % (year, image_set), 'w')
for image_id in image_ids:
    list_file.write('../../data/VOC%stest/JPEGImages/%s.jpg' %
                    (year, image_id))
    convert_annotation(year, image_id, list_file)
    list_file.write('\n')
list_file.close()
