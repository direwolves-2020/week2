def insertion_sort(arr):
	# """ sort list by comparing each value from left to right to the value of
	# its left neighbor/s until a left value is less than the number. Swap indices
	# for each comparison set in which left is greater than right. """


    for i in range(1, len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j]=arr[j], arr[j-1]
            j=j-1
            

    return arr

print (insertion_sort([11,3,6,1,20,10, 100, 7]))

assert insertion_sort([11,3,6,1,20,10, 100, 7]) == sorted([11,3,6,1,20,10, 100, 7])
assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
assert insertion_sort([9,8,7,6,5,4,3,2,1]) == [1,2,3,4,5,6,7,8,9]
