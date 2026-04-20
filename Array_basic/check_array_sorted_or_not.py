# we are given an array and it is sorted wheater in increasing order or decreasing order check it is ass or dsc.
def func(arr):
    for i in range(0 , len(arr)-1):
        if arr[i] > arr[i+1]:
            return "Sorted in descending order"
        return "Sorted in asscending order"