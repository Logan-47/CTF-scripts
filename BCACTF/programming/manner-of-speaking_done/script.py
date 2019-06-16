# -*- coding: utf-8 -*-
# @Author: logan47
# @Date:   2019-06-09 21:52:23
# @Last Modified by:   logan47
# @Last Modified time: 2019-06-09 22:56:16
import copy

list_of_commands = ["cadadddddr", 'caddadddddr', 'caadddddr', 'caddadddddr', 'cadddddddddddddddddddadddddr', 'cadddddadddddr', 'caaddddddr', 'cadddddddddddadddr', 'cadadr', 'cadddddadr', 'cadddddddadr', 'caddddaddddr', 'caddddddddadr', 'caddddadr', 'cadddddadr', 'cadddadr', 'cadddadddddr', 'caddddaddddr', 'cadddddddddddddddadddddr', 'cadddddddddddddddddadddr', 'caadr', 'caddddddadddddr', 'cadddddddddddddddddadddr', 'caddddadr', 'caddddddddddddadddr', 'caddddddddddddadddddr', 'cadadr', 'cadddddddddddddadddddr', 'caddddddadddr', 'caddddaddddr', 'cadadr', 'cadddddadr', 'caddddaddddr', 'caddddadr', 'caddddddddddddddddddddddadddddr', 'cadddadr', 'caddddddddddddddddddadddr', 'caadr', 'caddddddddddddadddr', 'caddddadddddr', 'cadar', 'caddaddddddr']

# (( !\"#$%&'\(\)*+,-./)(0123456789)(:;<=>?@)(ABCDEFGHIJKLMNOPQRSTUVWXYZ)(\[\\\]^_`)(abcdefghijklmnopqrstuvwxyz)(\{|\}~))

l = [[' ',"!","\"","#","$","%","&","'","(",")","*",'+'], [ "0","1", "2", "3", "4", "5", "6", "7", "8", '9'],[":",";","<","=",'>',"?","@"],["A","B","C","D","E","F","G","H","I",'J',"K","L","M","N","O","P",'Q',"R","S","T","U",'V','W',"X",'Y','Z'],["\[","\\","\]",'^',"_","`"],['a',"b","c","d","e","f","g","h","i","j","k","l","m",'n','o',"p","q","r","s","t","u",'v',"w","x","y","z"], ["\{",'|',"\}","~"]]

flag = []

for i in list_of_commands:
	temp_list = []
	
	# print("for: "+ i)
	
	cmd = i[1:-1][::-1]
	
	n_cmd = list(cmd)
	
	temp_list = copy.deepcopy(l)
	# temp_list = l[:]
	
	# print(temp_list)
	# print(temp_list)
	
	for i in n_cmd:
		mycmd = 'c'+i+'r'
		
		# print(mycmd)
		
		if mycmd == 'cdr':
			
			data1 = temp_list.pop(0)
			# print(data1)
		
		elif mycmd == 'car':
			
			temp_list = temp_list[0]
			# print(temp_list)
	flag.append(temp_list)

print(''.join(flag))





