#!/usr/bin/env python3

# Question: Given a string, check if it is a permutation of palindrome


def palindrome_per(string):
	new_string = string.strip().replace(" ","")		# String without spaces
	length = len(new_string)
	flag = 0

	# Loop to check if it is palindrome
	for char in new_string:
		if new_string[length-1] == char:	 # Letter from end of string compared to its pair from the beginning
			flag = flag + 1	
		else:
			pass
		length -= 1		# Moving one letter back at a time

	# Loop to check for permutation
	if flag == len(new_string):
		return True
	else:
		return False


if __name__ == "__main__":

	import sys
	if palindrome_per(sys.argv[-1]):
		print ("It is palindrome permutation")
	else:
		print ("It is not palindrome permutation")
	