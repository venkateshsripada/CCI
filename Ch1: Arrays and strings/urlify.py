#!/usr/bin/env python3

# Printing "%20" instead of space in a string. The end of string is to be ignored 

def replacing(string):

	new_string = string.strip().replace(" ","%20")
	return new_string

if __name__ == "__main__":
	
	import sys
	print (replacing(sys.argv[-1]))
