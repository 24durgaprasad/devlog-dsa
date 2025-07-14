def recursivebubblesort(nums, n):
    if n == 1:
        return nums

    for j in range(n - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return recursivebubblesort(nums, n - 1)

# Example usage
num1 = [7, 2, 3, 1, 6]
ans = recursivebubblesort(num1, len(num1)) 
print(ans)


# class Solution:
#     def bubbleSort(self, nums):
#         n = len(nums)
#         for i in range(n):
#             for j in range(n - i - 1):
#                 if nums[j] > nums[j + 1]:
#                     nums[j], nums[j + 1] = nums[j + 1], nums[j]
#         return nums

# # Example usage
# sol = Solution()
# nums = [5, 1, 4, 2, 8]
# print(sol.bubbleSort(nums))

