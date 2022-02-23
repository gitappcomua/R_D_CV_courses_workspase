# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:42:14 2022

@author: vova
"""

import os
import cv2
import pickle
import numpy as np
from matplotlib import pyplot as plt

writer = cv2.VideoWriter_fourcc(*'XVID')

cap = cv2.VideoCapture('data/mixkit-curvy-road-on-a-tree-covered-hill-41537.mp4');

# Let's assume the detector has detected the red vehicle
x1, y1 = 1018, 686
x2, y2 = 1102, 726

width = x2 - x1
height = y2 - y1

# Limit the search to a certain vicinity (since the cars can only move that fast)
search = 50

# Set up tracker
tracker_types = ['KCF', 'CSRT']
tracker_type = tracker_types[1]

if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
    out = cv2.VideoWriter('treker_result_KCF.mp4', writer, 25, (1920, 1080));

if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()
    out = cv2.VideoWriter('treker_result_CSRT.mp4', writer, 25, (1920, 1080));
    
    
    # Genrate tracking template
ret, frame = cap.read();
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
if ret == True:
    bbox = (x1, y1, width, height)
    ok = tracker.init(frame, bbox)
    

while(cap.isOpened()):
    ret, frame = cap.read();
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if ret == True:
        ok, bbox = tracker.update(frame)
        print(ok, bbox);
        # Show the tracker working
        x1, y1 = bbox[0], bbox[1]
        width, height = bbox[2], bbox[3];
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x1+width), int(y1+height)), (0, 255, 0), 2)
        img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imshow('Frame',img);
        out.write(img);
        cv2.waitKey(50);

    else:
        break
    
cap.release();
out.release();
cv2.destroyAllWindows();