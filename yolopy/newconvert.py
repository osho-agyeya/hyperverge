# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:56:37 2018

@author: Osho
"""

# In[]:
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import cv2
import re

from lxml import etree
import xml.etree.cElementTree as ET
import cv2
import os
import argparse



# In[]:
        
        
completePath="E:\\hyperverge\\yolopy\\yolov\\images\\"

#fi="16k_images"
fi="images"
#odir="data/testn/img"
fit="ground_truth"



imgs=os.listdir(fi)




#%%
def write_xml(saveDir, imagefolder, imagename, imgWidth, imgHeight, depth, bounding_boxes, pose="Unspecified"):
    annotation = ET.Element("annotation")
    ET.SubElement(annotation, 'folder').text = str(imagefolder)
    ET.SubElement(annotation, 'filename').text = str(imagename)
    ET.SubElement(annotation, 'path').text = str(completePath+imagename)
    
    source=ET.SubElement(annotation,"source")
    
    ET.SubElement(source,"database").text="Unknown"
    
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(imgWidth)
    ET.SubElement(size, 'height').text = str(imgHeight)
    ET.SubElement(size, 'depth').text = str(depth)

    ET.SubElement(annotation, 'segmented').text = '0'

    for box in bounding_boxes:
        obj = ET.SubElement(annotation, 'object')

        ET.SubElement(obj, 'name').text = str(box[0])
        ET.SubElement(obj, 'pose').text = str(pose)
        ET.SubElement(obj, 'truncated').text = '0'
        ET.SubElement(obj, 'difficult').text = '0'

        bbox = ET.SubElement(obj, 'bndbox')

        ET.SubElement(bbox, 'xmin').text = str(box[1])
        ET.SubElement(bbox, 'ymin').text = str(box[2])
        ET.SubElement(bbox, 'xmax').text = str(box[3])
        ET.SubElement(bbox, 'ymax').text = str(box[4])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)

    ind=imagename.find('.')

    save_path =  saveDir+"/"+ imagename[0:ind]+".xml"

    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)



# In[]:

for imgi in imgs:
    im=cv2.imread(fi+"/"+imgi)
    height = im.shape[0]
    width = im.shape[1]
    depth = im.shape[2]


    bbox=[]
    
    ind=imgi.find('.')
    infname="gt_"+imgi[0:ind]+".txt"
    fpi=fit+"/"+infname
    #fpo=odirt+"/"+infname
    #fwrite=open(fpo,"w")
    fread=open(fpi)
    line=fread.readline()
    while line:
        lina=re.split(", |,| ",line)
        xmin=int(lina[0])
        ymin=int(lina[1])
        xmax=int(lina[2])
        ymax=int(lina[3])
        word=str(lina[4])
        #ns=str(xminn)+", "+str(yminn)+", "+str(xmaxn)+", "+str(ymaxn)+", "+word
        bbox.append(["words",xmin,ymin,xmax,ymax])
        #fwrite.write(ns)
        line=fread.readline()
    fread.close()
    write_xml("annonations", "images",imgi, width, height, depth, bbox, pose="Unspecified")
    #fwrite.close()
        
        
    #print(im.shape)
    #break
    
    
#print(im)
#print(im.shape)
# In[]:
#set_x=np.array(set_x)

# In[]:
#print(set_x[0].shape)
 # In[]:
 
#f=open("osho.pickle","wb")
#pickle.dump(set_x,f,protocol=pickle.HIGHEST_PROTOCOL)
#f.close()
 # In[]: 