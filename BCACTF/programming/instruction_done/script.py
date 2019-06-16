# -*- coding: utf-8 -*-
# @Author: logan47
# @Date:   2019-06-09 13:04:44
# @Last Modified by:   logan47
# @Last Modified time: 2019-06-09 13:31:15

mylist = [20, 30, 8, 14, 17, 24, 44, 19, 17, 29, 20, 34, 35, 27, 42, 34, 7, 25, 7, 21, 8, 38, 13, 25, 14, 13, 42, 14, 20, 23, 3, 27, 38, 9, 18, 41, 3, 11, 35]

flag = []
flag1 = []
listcount = 0
filepath = 'flag.txt'  

with open(filepath) as f:
	for line in f:
		line = line.strip()
		# print(line)
		if ((len(line) % 3)==0) & ('&' not in line):
			line_index = mylist[listcount]
			flag.append(line[line_index - 1])
			flag1.append(line[line_index])

			listcount = listcount + 1

print("".join(flag))