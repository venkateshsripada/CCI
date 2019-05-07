#!/usr/bin/env python3

# https://www.geeksforgeeks.org/merge-sort/

def mergesort(arr):
	if len(arr) > 1:
		mid = int(len(arr)/2)	# Dividing the array into two
		L = arr[:mid]	#All elements to the left of mid
		R = arr[mid:]	# All elements to the right of mid

		mergesort(L)
		mergesort(R)

		i = j = k = 0

		while i < len(L) and j < len(R):	# Note that this loop is the main sub sorting loop as elements in a particular L and R are sorted 
			if L[i] < R[j]:		# Checks for each element in L with those in R.  
				arr[k] = L[i]
				i+= 1
			else:
				arr[k] = R[j]
				j+= 1
			k += 1

		# These two loops add both the sorted left and right arrays
		while i < len(L):	
			arr[k] = L[i]
			i+=1
			k+=1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

def printList(arr):
	for i in range(len(arr)):
		print (arr[i], end =" ")

if __name__ == "__main__":
	arr = [12,11,13,5,6,7]
	print ("Given array is: \n", arr)
	print ("sorted array is \n")
	mergesort(arr)
	printList(arr)