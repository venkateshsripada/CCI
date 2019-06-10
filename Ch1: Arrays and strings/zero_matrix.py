#!/usr/bin/env python3


def zero_matrix(matrix):
	dimension_row = []
	dimension_col = []

	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == 0:
				dimension_row.append(i)	# All rows to be zeroed
				dimension_col.append(j)	# All columns to be zeroed
	

	# Loop to zero all rows
	for row in dimension_row:	# Checking which rows are to be zeroed
		for col in range(len(matrix[0])):
			matrix[row][col] = 0
		
	# Lopp to zero all columns
	for col in dimension_col:	# Checking which columns are to be zeroed
		for row in range(len(matrix)):
			matrix[row][col] = 0
	
	return (matrix)

if __name__ == "__main__":

	matrix = ([1,2,3,2],[4,5,6,7],[2,0,1,0])
	print (zero_matrix(matrix))
