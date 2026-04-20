def func(nums, target):
    count = 0
    for i in range(len(nums)):
        if nums[i] == target:
            count += 1
    return count

arr = [1,2,3,3,4]
print(func(arr , 3))
