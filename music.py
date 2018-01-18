# *-* coding: utf-8 -*-

import os
from PIL import Image

#currentscreen
#C:\Users\koutsuken1\python\Music
def get_picture():
	global name
	#test name : 'test.png' 
	name = 'musicscreencap'
	cmd1 = 'adb shell screencap -p /sdcard/%s.png' % name
	cmd2 = 'adb pull /sdcard/%s.png C:\Users\koutsuken1\python\cloudmusickuaijing\%s.png'% (name,name)
	cmd3 = 'adb shell rm /sdcard/%s.png' % name
	os.system(cmd1)
	os.system(cmd2)
	os.system(cmd3)

def swipe(user_input,position):
	if user_input == ',':
		position[2] -= 6 
	if user_input == '.':
		position[2] += 0 
	cmd4 = 'adb shell input swipe {x1} {y1} {x2} {y2} 100'.format(
	x1 = position[0],
	y1 = position[1],
	x2 = position[2],
	y2 = position[3])
	os.system(cmd4)

swipe_x1 = 5
swipe_x2 = swipe_x1 + 3
swipe_y1 = 1600
swipe_y2 = 1600

def find_button(im):
	global swipe_x1, swipe_y1, swipe_x2, swipe_y2
	pixel = im.load()
	for i in range(120,950):
		if pixel[i,1600] == (255,255,255,255):
			swipe_x1 = i
			swipe_x2 = swipe_x1 + 30
			break
	return [swipe_x1,swipe_y1,swipe_x2,swipe_y2]

def main():
	while True:
		user_input = raw_input('front(.) or back(,) : ')
		get_picture()
		im = Image.open('C:\Users\koutsuken1\python\cloudmusickuaijing\%s.png'% name) 
		position = find_button(im)
		swipe(user_input,position)


if __name__ == '__main__':
	main()