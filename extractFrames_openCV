# -------------------------
# Author : PythosLabs.com
# About : This scripts takes in a video and converts all the frames in to images
# Date Created : 17 Oct 2017
#
# Modifications
# -------------------------

import numpy as np
import cv2

video_location = "./videos1/bug1.mp4"
output_folder = "./output/"

cap = cv2.VideoCapture(video_location)
ret = 1
frame_number=477
#while(cap.isOpened()):   # This is not working
while(ret):
    frame_number += 1
    #print("Now reading time: " + str(seconds_elapsed) + str(ret))
    #cap.set(cv2.CAP_PROP_POS_MSEC, seconds_elapsed*1000);

    ret, frame = cap.read()
    print("Frame # " + str(frame_number)+ " converted =" + str(ret))
    out_k2 = cv2.imwrite(output_folder + "im_" + str(frame_number) + ".jpg", frame)

cap.release()
