


def binary_search(arr, number):
	""" iterate through an array by finding middle index, comparing <> and 
	then slicing index up to or after the middle of each subsequent index """


##sample dataset
arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]


assert binary_search(arr, 66) == True, '66 should be True'
assert binary_search(arr, 5854) == True, '5854 should be True'
assert binary_search(arr, 239) == True, '66 should be True'
assert binary_search(arr, 999) == False, '999 should be False'



