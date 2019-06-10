#!/usr/bin/env python3


def rotate_matrix(matrix):
	
	matrix = matrix[::-1] 	# Reverses the tuple

	A = len(matrix)

	# Loop to rotate matrix
	for i in range(A-1):	
		for j in range(A-i-1):	# Begins counting from last as first and last elements are to be swapped
			matrix[i][j], matrix[A-j-1][A-i-1] = matrix[A-j-1][A-i-1], matrix[i][j]


	return (matrix)

		

if __name__ == "__main__":
	

	sample1 = ([1,2],[3,4])
	ans_sample1 = ([2,4],[1,3])
	sample1 = rotate_matrix(sample1)
	assert sample1 == ans_sample1



	sample2 = ([1,2,3],[4,5,6],[7,8,9])
	ans_sample2 = ([3,6,9],[2,5,8],[1,4,7])
	sample2 = rotate_matrix(sample2)
	assert sample2 == ans_sample2



