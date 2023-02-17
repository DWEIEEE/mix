#!/usr/bin/env python
# coding: utf-8

# In[29]:


import os
import cv2
import glob

video_path = input("Enter your video path：")
output_folder = input("Enter your video output path:")
pick_fps = int(input("fps for getting image from video："))
#video_path = 'C:/Users/DWEI/Desktop/Aiunion/PPECheck_v10_demo.mp4'
#output_folder = 'C:/Users/DWEI/Desktop/Aiunion/vg_image/'
#pick_fps = 6
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

vc = cv2.VideoCapture(video_path)
fps = vc.get(cv2.CAP_PROP_FPS)
print("video's fps:",fps)
frame_count = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
print('total frame:',frame_count)

n = round(fps/pick_fps)
for idx in range(0,frame_count,n):
    vc.set(1, idx)
    ret, frame = vc.read()
    height, width, layers = frame.shape
    size = (width, height)

    if frame is not None:
        file_name = '{}{:04d}.jpg'.format(output_folder,round((idx+1)/n)+1)
        cv2.imwrite(file_name, frame)

    print("\rprogress rate: {}/{}".format(round((idx+1)/n)+1,round(frame_count/n)), end = '')
vc.release()


# In[ ]:




