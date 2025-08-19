# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

nums = [[1,1,1],[1,0,1],[1,1,1]]

zero_positions = []

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] == 0:
                zero_positions.append([i,j])
               

for i,j in zero_positions:                    
            
 for col in range(len(nums[0])):
     nums[i][col] = 0   
 for row in range(len(nums)):
     nums[row][j] = 0               

         


print(nums)        



   
         

       