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



# In[]:

#fi="16k_images"
fi="data/test/img"
odir="data/testn/img"
fit="data/test/inf"
odirt="data/testn/inf"

set_x=[]
imgs=os.listdir(fi)


# In[]:
#k=0
ii=[]
for imgi in imgs:
    im=cv2.imread(fi+"/"+imgi,3)
    y_ = im.shape[0]
    x_ = im.shape[1]
    
    targetSize = 608
    x_scale = targetSize / x_
    y_scale = targetSize / y_
    #print(x_scale, y_scale)
    img2 = cv2.resize(im, (targetSize, targetSize));
#    k=k+1
#    if k==8000:
#        break
#    print(im)
    #plt.plot(im)
    #plt.imshow(im)
    #print(im.shape)
#    if(len(im.shape)<=2):
#        print(im.shape)
#        continue
#    if(im.shape[2]<=2):
#        print(im.shape)
#        continue
    cv2.imwrite(odir+"/"+imgi,img2)
    ind=imgi.find('.')
    infname="gt_"+imgi[0:ind]+".txt"
    fpi=fit+"/"+infname
    fpo=odirt+"/"+infname
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
        xminn=int(np.round(xmin * x_scale))
        yminn=int(np.round(xmax * y_scale))
        xmaxn=int(np.round(xmax * x_scale))
        ymaxn=int(np.round(ymax * y_scale))
        ns=str(xminn)+", "+str(yminn)+", "+str(xmaxn)+", "+str(ymaxn)+", "+word
        fwrite.write(ns)
        line=fread.readline()
    fread.close()
    fwrite.close()
        
        
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