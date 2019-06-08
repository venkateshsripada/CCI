#!/usr/bin/env python3

# Question: Edits that can be performed on a string are insert, remove or replace a character. Check if more than one are to be performed

def away(string1, string2):
	new_string1 = string1.strip()
	new_string2 = string2.strip()

	if len(new_string1) > len(new_string2):
		max_string  = new_string1
		min_string = new_string2

	else:
		max_string = new_string2
		min_string = new_string1

	i = 0
	flag = 0
	if len(max_string) > len(min_string) + 1:
		return False

	else:
		max_string = max_string.split().sort()
		min_string = min_string.split().sort()

		print ("max_string", max_string)
		print ('min_string', min_string)
	

		for char in min_string:

			if char == max_string[i]:
				pass
			else:
				flag += 1
			i += 1

		if flag <= 1:
			return True
		else:
			return False

if __name__ == "__main__":

	import sys
	if away(sys.argv[-2], sys.argv[-1]):
		print ("Strings are just one away")
	else:
		print ("Strings need more edits")

