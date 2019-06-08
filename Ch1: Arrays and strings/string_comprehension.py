#!/usr/bin/env python3

def compress(string):

	sorted_string = sorted(string)
	length = len(sorted_string)
	number = str()

	count = 1

	# Loop to check if there is a repetition of the letter in string
	for i in range(len(sorted_string)):

		if i >= 0 and i <= length-2 and sorted_string[i] == sorted_string[i+1]:		# Checking for corner conditions 
			count = count + 1	# increase counter as letter is being repeated
			
		else:
			number = number + sorted_string[i]
			number = number + str(count)	# add the letter and value before recounting for new letter 
			count = 1	# Reinitialize counter for new letter

	# Loop to check if new string is concatenated better or not
	if len(number) >= length:
		return (string)

	else:
		return (number)

if __name__ == "__main__":

	import sys

	# Check in input is only letters
	for i in sys.argv[-1]:
		if i.isdigit():
			raise Exception("Type error: input only letters")


	print (compress(sys.argv[-1]))