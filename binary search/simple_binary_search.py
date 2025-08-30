# # nums = list(map(int,input("enter array in asscending order :").split()))
# # target = int(input("enter a target value :"))

# # if target not in  nums:
# #      print(-1) 
# # for i  in range(len(nums)-1):
# #  if nums[i] == target:
# #         print(i)
   

# class Solution:
#     def search( nums, target):
# #         if target not in  nums:
# #           return -1 
# #         for i  in range(len(nums)-1):
# #          if nums[i] == target:
# #                 print(i)
              
               

# # nums = list(map(int,input("enter array in asscending order :").split()))
# # target = int(input("enter a target value :"))

# # Solution.search(nums,target)
            
class Solution:
    def search(nums, target):
        low, high = 0, len(nums) - 1  

        while low <= high:  
            mid = (low + high) // 2  

            if nums[mid] == target:  
                return mid  
            elif nums[mid] < target:  
                low = mid + 1  
            else:  
                high = mid - 1  

        return -1   


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution.search(nums, target))  










