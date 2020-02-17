def merge_sort(arr):
    print('splitting', arr)
    if len(arr)>1:
        m=len(arr)//2
        left_arr=arr[:m]
        right_arr=arr[m:]
        merge_sort(left_arr)
        merge_sort(right_arr)


        i=0
        j=0
        k=0

        #sorting
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k]=left_arr[i]
                i=i+1
            else:
                arr[k]=right_arr[j]
                j=j+1
            k=k+1

        #merging
        while i < len(left_arr):
            arr[k]=left_arr[i]
            i=i+1
            k=k+1

        while j < len(right_arr):
            arr[k]=right_arr[j]
            j=j+1
            k=k+1

    print('merging', arr)



#arr=[98, 744, 28, 81, 446, 2, 5, 10, 99, 55]
arr=[98, 744, 82, 36]
merge_sort(arr)
print("Sorted list", arr)
