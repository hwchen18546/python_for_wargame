#!/usr/bin/env python

#dir+file name
import glob
#lists1 = glob.glob('/home/hwchen18546/ROPgadget/*.py')
lists1 = sorted(glob.glob('/home/hwchen18546/Desktop/Misc75/*'))
 
for item in lists1:
    #print item
    with open(item, 'r') as content_file:
        content = content_file.read()
    print content.decode('hex'),
print
#c{352dc0cf9c7efdf560dbb5ued17we7n2Pe}emi

import hashlib
for i in range(0,40):
    FileName = hashlib.md5(str(i)).hexdigest()
    Directory = '/home/hwchen18546/Desktop/Misc75/'+FileName
    with open(Directory, 'r') as content_file:
        content = content_file.read()
    print content.decode('hex'),
print
#Pwnium{02cef7eeb75fdd9dfc67c0dc1e3e255b}

#file name
import os
lists2 = os.listdir('/home/hwchen18546/Desktop/Misc75/')
