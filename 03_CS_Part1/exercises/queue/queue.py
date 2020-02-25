



class Node:

	def __init__(self, data=None):
		self.data = data
		self.right = None
		self.length = 0



class Queue:

	def __init__(self):
		self.first = None
		self.last = None

	# def is_empty(self):
	# 	print ('empty')
	# 	return self.length == 0


	def append(self, value):
		""" add value to left most position of list """

		new_node = Node(value)
		# self.length += 1

		if self.first == None:  # If list is empty
			self.first = new_node # Make new node the first value
			self.last = new_node # Make new node the last value
			print ('first value added ',value)

		else:    # If list not empty
			self.last.right = new_node   # Set right value to new value
			self.last = new_node    # Make new node the last value
			print ('new value appended', value)
		return value



	def pop(self):
		print ('\n')
		""" return the right-most value if one exists and set its left neighbor to first """

		if self.first == None:  # If empty list return false
			print ('empty')
			return None

		else:   # If list not empty
			data = self.first.data 
			neighbor = self.first.right
			# self.length -= 1

			if neighbor is None: # If there are no more items in list
				print ('neighbor is none')
				self.first = None # set first and last to none
				self.last = None

			else:
				print ('first ', self.first.data)
				self.first = neighbor # Replace first spot with neighbor
				print ('neighbor: ', neighbor.data)
			print ('returned', data)
			return data





test1 = Queue()
# test1.is_empty()
assert test1.append(3) == 3
assert test1.append(4) == 4
assert test1.append(5) == 5

assert test1.pop() == 3
assert test1.pop() == 4
assert test1.pop() == 5
assert test1.pop() == None


