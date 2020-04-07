# COMP 2700
# Spring 2020
# Lab 2
# kbrleson
  
# Question 1
def matrix_print(A):
	for row in A:
		for item in row:
			print('%i ' % item, end='')
		print('\n')


# Question 2
def matrix_add_boolean(A, B):
	result = [ [0]*len(A[0]) for i in range(len(A)) ]
	
	for row_index, row in enumerate(A):
		for index, value in enumerate(row):
			if value == 0 and B[row_index][index] == 0:
				result[row_index][index] = 0
			else:
				result[row_index][index] = 1
	
	return result

# Question 3
def matrix_multiply_boolean(A, B):
	result = [[0 for row in range(len(A))] for col in range(len(B[0]))]
	
	for row_index in range(len(A)):
		for col_index in range(len(B[0])):
			for col_row_index in range(len(B)):
				if(result[row_index][col_index] >= 1):
					result[row_index][col_index] = 1
					continue
				else:
					result[row_index][col_index] = result[row_index][col_index] + A[row_index][col_row_index] * B[col_row_index][col_index]
			
	return result

# Question 4
def matrix_power(A, n):
	if (n == 2):
		result = matrix_multiply_boolean(A, A)
	else:
		result = matrix_multiply_boolean(A, A)
		for i in range(n - 1):
			result = matrix_multiply_boolean(copy.deepcopy(result), A)
		
		
	return result
	
# Question 5
def transitive_closure(A):
	result = A
	
	for i in range(len(A[0]) - 2):
		result = matrix_add_boolean(result, matrix_power(A, i))

	return result
	
	
if __name__ == '__main__':
	print("----------------------[Question 1]----------------------")
	print("Let R")
	R = [[0, 0, 0, 1], [0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
	print(R)
	print("--------------------------------------------------------")
	

	print("Output of 'matrix_print(R)' ")
	matrix_print(R)
	print("\n\n")
	
	
	print("----------------------[Question 2]----------------------")
	print("Let A")
	A = [[0, 1], [1, 0]]
	print(A)
	print("--------------------------------------------------------")
	
	
	print("Let B")
	B = [[1, 0], [1, 0]]
	print(B)
	print("--------------------------------------------------------")
	
	print("Output of 'matrix_add_boolean(A, B)' ")
	print(matrix_add_boolean(A, B))
	print("\n\n")


	print("----------------------[Question 3]----------------------")
	print("Let A")
	A = [[0, 1, 1], [1, 0, 1]]
	print(A)
	print("--------------------------------------------------------")
	
	print("Let B")
	B = [[1,0], [0,0], [0,1]]
	print(B)
	print("--------------------------------------------------------")

	print("Output of 'matrix_multiply_boolean(A, B)' ")
	print(matrix_multiply_boolean(A, B))
	print("\n\n")
	
	
	print("----------------------[Question 4]----------------------")
	print("Let R")
	print(R)
	print("--------------------------------------------------------")
	

	print("Output of 'matrix_power(R, 2)' ")
	print(matrix_power(R, 2))
	print("\n\n")
	
	
	print("----------------------[Question 5]----------------------")
	print("Let R")
	print(R)
	print("--------------------------------------------------------")
	

	print("Output of 'transitive_closure(R)' ")
	print(transitive_closure(R))
	print("\n\n")