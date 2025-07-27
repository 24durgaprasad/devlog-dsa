# Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray.
# A subarray is a contiguous non-empty sequence of elements within an array.

nums = list(map(int,input("eneter array elements:").split()))

max_so_far = nums[0]
max_last_index = nums[0]

for i in range(1,len(nums)):
    max_last_index = max(nums[i],max_last_index+nums[i])
    max_so_far = max(max_so_far,max_last_index)

print(max_so_far)    