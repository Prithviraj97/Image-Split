# This code splits a side-by-side view image into two pieces. When using Stereo camera to record a video we often get the result as side-by-side view i.e. left and right frames
# together. We can appropriately split the joint frame into 2 using the openCV. 
#Prithvi R. Singh

#!pip install natsort
from natsort import natsorted
import matplotlib.pyplot as plt
import cv2
import os
import glob
import sys
import shutil

file_root = " ..//Frame"
data_root = " ..//Frame2"

#One can also use the split-image package to split image into multiple parts. https://pypi.org/project/split-image/
images = []
count = 0
#provide the full path of the image/frame folder. The /*.png tell the program to read all files with .png extension.
#natsorted is used to sort the accessibilty of image streaming to program from folder.
for filename in natsorted(glob.glob("..//*.png")):
    #sucess = True
    if filename.endswith(".png"): #not really necessary to have in this code.
        img = cv2.imread(filename)
    height = img.shape[0]
    width = img.shape[1]
    wid_cut = width // 2
        
    s1 = img[:, :wid_cut]
    #s2 = img[:, wid_cut:]
    images.append(s1)
    #for i in s1:
    cv2.imwrite(data_root + '%d.png' %(count), s1) #s1 is the left side of the image. 
    #cv2.imwrite(data_root2 + '%d.png' %(count), s2) //data_root2 should be another or same folder to store right side image
    count += 1

#to view the image that is also appended to images as a list we can use matplotlib, scipy, PIL.
plt.imshow(images[0]) # show the image based on index.