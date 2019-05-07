#!/usr/bin/env python3

# Question: Given two strings, write a method to check if permuatation of other


def permutation(string1, string2):
	if len(string1) > len(string2):
		max_string = string1
		min_string = string2
	else:
		max_string = string2
		min_string = string1


	for char in min_string:
		if char in max_string:
			return True
		else:
			return False

	

if __name__ == "__main__":
	print ("Type first string")
	string1 = input()
	print ("Type second string")
	string2 = input()

	if permutation(string1, string2) is True:
		print ( "Two strings are permutations of each other")

	else:
		print ("The two strings are not permuatation of each other")