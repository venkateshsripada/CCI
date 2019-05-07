#!/usr/bin/env python3

# Q: Implement algorithm to determine if string has all unique characters.   

#-------------------------------------------------------------
'''Solution using additional datasets'''

# set_string = set(string) 

# if len(string) != len(set_string):
# 	print ("The string is not unique")

# else:
	# print ("String is unique")
#--------------------------------------------------------------

# Solution without using additonal datasets

def unique(string):

	new_string = []
	flag = 0

	for char in string:
		
		if char in new_string:
			flag = flag+1
		new_string.append(char)

	return flag



if __name__ == "__main__":

	print ("Type a string")
	string = input()
	num = unique(string)


	if num >= 1:
		print ("The string is not unique")
	else:
		print ("string is unique")



