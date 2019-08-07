#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:43:49 2019

@author: sidv88
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 15:42:25 2019

@author: sidv88
"""
#reference link - https://www.geeksforgeeks.org/rename-multiple-files-using-python/
import os

#Function to rename multiple files
def main():
    i = 0
    
    for filename in os.listdir("/Users/sidv88/Documents/yolo_folder/ocr/ocr/"):
        dst = str(i) + ".jpg"
        src = "/Users/sidv88/Documents/yolo_folder/ocr/ocr/" + filename
        dst = "/Users/sidv88/Documents/yolo_folder/ocr/ocr/" + dst
        
        #rename function to rename all the files
        os.rename(src, dst)
        i += 1
        
if __name__ == '__main__':
    main()