class Solution:
    def rotateArrayByOne(self, nums,k):
        m = k % len(nums)
        print(nums[-m:]+nums[:-m])

sol = Solution()
nums = [1,2,3,4,5,6,7,8]
sol.rotateArrayByOne(nums,3)

