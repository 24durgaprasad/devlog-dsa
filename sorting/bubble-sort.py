nums = [7, 4, 1, 5, 3]

for i in range(len(nums)):
    for j in range(len(nums) - 1):  
        if nums[j] > nums[j+1]:
            temp = nums[j+1]
            nums[j+1] = nums[j]
            nums[j] = temp

print(nums)  
