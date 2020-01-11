#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 mayilong <mayilong@mayilong.local>
#
# Distributed under terms of the MIT license.

import numpy as np
import cv2
import time
cap = cv2.VideoCapture('../277425776.mp4')
time.sleep(5)
print(cap.isOpened())
while(True):
	#capture frame-by-frame
    ret , frame = cap.read()
    
    #our operation on the frame come here
    # gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    
    #display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
    	break
#when everything done , release the capture
# cap.release()
# cv2.destroyAllWindows()
