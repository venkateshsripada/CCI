#!/usr/bin/env python3

# Question: Given two strings, write a method to check if permuatation of other

# Optimal solution1:

def opt_permutation(string1, string2):
	if len(string1) == len(string2):
		string1 = string1.split()
		string1 = string1.sort()
		string2 = string2.split()
		string2 = string2.sort()
		if string1 == string2:
			return True
		else:
			return False
	else:
		return False


# Solution 2:
def permutation(string1, string2):
	if len(string1) == len(string2):
		for char in string1:
			if char in string2:
				return True
			else:
				return False
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