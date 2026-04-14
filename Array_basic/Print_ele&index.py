# WE have to print the element and its index in the array(we are making a functions for it)
# 1st method
def func(arr):
    for idx, val in enumerate(arr):
        print(idx , val , end="")
    
arr = [1,2,3]
func(arr)

#2nd method

def func(arr):
    for i in range(len(arr)):
        print(f"idx {i} , value {arr[i]}")
    
arr = [1,2,3]
func(arr)
    



