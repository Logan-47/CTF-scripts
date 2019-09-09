# -*- coding: utf-8 -*-
# @Author: logan47
# @Date:   2019-09-08 18:27:06
# @Last Modified by:   logan47
# @Last Modified time: 2019-09-08 22:59:52
from PIL import Image
im = Image.open("alphinity.png", 'r')
pix_val = list(im.getdata())
al = []
# print(pix_val)

for i in pix_val:
	if i[3] == 255:
		al.append(0)
	elif i[3] == 254:
		al.append(1)
	else:
		pass

print(''.join([str(x) for x in al]))
# convert binary to => text
#AFFCTF{h3ll0_4ff1n17y}
