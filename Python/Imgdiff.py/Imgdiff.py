#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:30:13 2020

@author: dass
"""

import cv2
path = r'/home/dass/Downloads/70.jpg'
img = cv2.imread(path,0) 
cv2.imshow('image', img)
