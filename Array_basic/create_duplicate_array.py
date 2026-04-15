# Wrong way to create duplicate array
# arr = [1,2,3,4]
# arr2 = arr
# print(arr2)  #output [1, 2, 3, 4]
# arr2[0] = 10
# print(arr)   #output [1, 2, 3, 4]
# print(arr2)  #output [1, 2, 3, 4]

# Right way

arr = [1,2,3,4]
arr2 = arr.copy()
arr2[0] = 10
print(arr)
print(arr2)