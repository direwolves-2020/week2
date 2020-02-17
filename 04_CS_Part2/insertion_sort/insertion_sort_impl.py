


def insertion_sort(arr):
	""" sort list by comparing each value from left to right to the value of 
	its left neighbor/s until a left value is less than the number. Swap indices 
	for each comparison set in which left is greater than right. """

	# create range of array length
	index_range = range(0, len(arr))

	# iterate through array by index
	for index in index_range:  

		number = arr[index] # number to be inserted

		# if left neighbor is greater than number look through 
		while arr[index-1] >= number and index > 0:

			# swap left-right to right-left
			arr[index-1], arr[index]  = number, arr[index-1]

			# look left again
			index -= 1

	return arr


assert insertion_sort([11,3,6,1,20,10, 100, 7]) == sorted([11,3,6,1,20,10, 100, 7])
assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
assert insertion_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]



