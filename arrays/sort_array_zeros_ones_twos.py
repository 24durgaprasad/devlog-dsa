# # Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.

# nums = list(map(int,input("enter array elements").split()))

# # print(sorted(nums))
# count_z = 0
# count_o = 0
# count_t = 0

# res = []


# for i in range(len(nums)):
#     if nums[i] == 0:
#         count_z+=1
#     elif nums[i] == 1:
#         count_o+=1
#     else :
#         count_t+=1

# for i in range(count_z):
#     res.append(0)
# for i in range(count_o):
#     res.append(1)
# for i in range(count_t):
#     res.append(2) 

# print(res)



from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
