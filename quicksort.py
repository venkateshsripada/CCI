#!/usr/bin/env python3

# https://www.geeksforgeeks.org/quick-sort/

def partition(arr, low, high):
	i = low - 1
	pivot = arr[high]

	# This is main swapping loop
	for j in range(low, high):
		if arr[j] <= pivot:	# If current element is lesser than pivot then swap
			i = i + 1	# Increment index of smaller element
			arr[i], arr[j] = arr[j], arr[i]

	# Once all elements are swapped the last unswapped and pivot are left which are swapped now
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quicksort(arr, low, high):
	# This is function to do quick sort

	if low < high:
		pi = partition(arr, low, high)	# pivot partition
		quicksort(arr, low, pi-1)	# Partitioning lesser than pivot elements
		quicksort(arr, pi+1, high)	# Partitioning greater than pivot elements


if __name__ == "__main__":

	arr = [10,7,8,9,1,5]
	n = len(arr)
	print ("length =", n)
	quicksort(arr,0,n-1)
	print ("sorted array is:")
	for i in range(n):
		print ("%d" %arr[i])


