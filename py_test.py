import numpy as np
import random

def fill_matrix():
	new_matrix = np.zeros((10,10),dtype=np.float)
	
	#Select rows and columns
	rows = new_matrix.shape[0]
	columns = new_matrix.shape[1]
	
	for row in range(0,rows):
		for col in range(0,columns):
			new_matrix[row,col] = random.randint(0,40)
	
	print(new_matrix)
	
if __name__ == "__main__":
	fill_matrix()
