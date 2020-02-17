



def quicksort(array):
	""" Starting with left-most item as the pivot value,
	find all values less than the pivot and partition them left in 
	the first half quicksort recursion, find all values greater than pivot 
	and partition them right in the second half recursion.

	If any remaining values are less than the pivot, then the right-most of the 
	less-than items becomes the new pivot.
	If no value is higher than the pivot, new pivot is left-most value
	"""



alist = [10, 20, 50, 30, 2, 5, 6,8,3,5,3,2,3,6,2,1,3,6,7,8,3,4]

assert quicksort(alist) == sorted(alist)



