class Solution:
    def selectionSort(self, nums):
        for i in range(len(nums)):
            min_num = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[min_num]:
                    min_num = j
            nums[i], nums[min_num] = nums[min_num], nums[i]
        
        return nums

s = Solution()

arr = list(map(int, input("Enter space-separated numbers: ").split()))


s1 = s.selectionSort(arr)
print(s1)




  



    