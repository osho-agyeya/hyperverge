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

import os
from os import walk, getcwd
from PIL import Image

from lxml import etree
import xml.etree.cElementTree as ET
import cv2
import os
import argparse


# In[]:

#fi="16k_images"
fi="gt/images"
#odir="g"
fit="gt/ground_truth"
odirt="gtnn"

set_x=[]
imgs=os.listdir(fi)


    
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

# In[]:
#k=0
ii=[]
for imgi in imgs:
    img_path=fi+"/"+imgi
    im=Image.open(img_path)
    w= int(im.size[0])
    h= int(im.size[1])

    ind=imgi.find('.')
    infname="gt_"+imgi[0:ind]+".txt"
    fpi=fit+"/"+infname
    fpo=odirt+"/"+imgi[0:ind]+".txt"
    fwrite=open(fpo,"w")
    fread=open(fpi)
    line=fread.readline()
    while line:
        lina=re.split(", |,| ",line)
        xmin=int(lina[0])
        ymin=int(lina[1])
        xmax=int(lina[2])
        ymax=int(lina[3])
        word=str(lina[4])
        
        b = (float(xmin), float(xmax), float(ymin), float(ymax))
        bb = convert((w,h), b)
        
        ns=str(0) + " " + " ".join([str(a) for a in bb])
        ns=ns+"\n"
        fwrite.write(ns)
        line=fread.readline()
    fread.close()
    fwrite.close()
        
#%%


#%%