#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 12:39:24 2019

@author: sidv88
"""
#reference link - https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
import os
if not os.path.exists("/Users/sidv88/documents/CVAT_Annotation/first_100/"):
    os.makedirs("/Users/sidv88/documents/CVAT_Annotation/first_100/")