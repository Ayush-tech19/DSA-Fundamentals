def func(arr):
    sum = 0
    product = 1
    for i in range(0 , len(arr)):
        sum += arr[i]
        product *= arr[i]
    return [sum , product]


arr = [1,2,4]
print(func(arr))