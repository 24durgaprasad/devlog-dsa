# class Solution:
#     def isSorted(self, nums):
#         if nums == sorted(nums):
#             return True
#         else:
#             return False
        
# nums = [2,1,1,2,3,4]
# print(Solution.isSorted(None,nums))

class Solution:
    def isSorted(self, nums):
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return False
        return True
nums = [1,1,2,3,4]
sol = Solution()
print(sol.isSorted(nums))
