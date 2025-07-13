# largest number in array-----------------------------------------------------------------------------------------------

# nums = [4,1,2,6,7,3]

# largest = nums[0]

# for i in range(len(nums)):
#     if nums[i] > largest:
#         largest = nums[i]
# print(largest)  

# second largest in array---------------------------------------------------------------------------------------------

# nums = [2,4,7,8,6]

# nums.sort(reverse=True)  


# for num in nums:
#     if num < nums[0]:
#         second_largest = num
#         break

# print(second_largest)

nums = [2, 4, 7, 8, 6]

first = second = float('-inf')

for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and second != first:
        second = num

print(second)





      



