


import random



class Board_Game:
	""" Create and navigate nested arrays """

	def __init__(self):
		self.board = [[4,6,8],[40,60,80],[400,600,800]]. # create board

	def print_board(self):
		print ('board:')
		print (self.board)

	def get_row(self,row):
		""" return row with index of value passed """
		return (self.board[row]) 

	def get_column(self, column):   
		""" return column with index of value passed """
		col = []
		for row in self.board:
			col.append(row[column])
		return (col)

	def get_coordinates(self, value):
		""" get row and column index of passed value and return as x,y tuple """
		for row in self.board:
			if value in row:
				row_index = (row.index(value))
				column_index = (self.board.index(row))
				return (row_index,column_index)
		return 0
	
	def get_surround(self,value):
		""" return all values except for the value passed """
		surrounding_values = []
		for row in self.board:
			for i in row:
				if i != value:
					surrounding_values.append(i)
		return surrounding_values





test1 = Board_Game()
test1.print_board()
assert test1.get_row(1) == [40, 60, 80]
assert test1.get_column(1) == [6,60,600]
assert test1.get_coordinates(60) == (1,1)
assert test1.get_surround(60) == [4, 6, 8, 40, 80, 400, 600, 800]

