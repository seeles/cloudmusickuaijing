# *-* coding: utf-8 -*-

import os
from PIL import Image



im = Image.open('./1.png')
a = im.load()
print a[1,1][1]
for i in range(120,950):
	print i
	print a[i,1600]
	if a[i,1600] == (255,255,255,255):
		print 1
		break
