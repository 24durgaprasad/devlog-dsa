nums = [7, 4, 1, 5, 3]

for i in range(1,len(nums)-1):
    key = nums[i]
    j = i - 1 
    while j >= 0 and nums[j] > key:
        nums[j+1] = nums[j]
        j -=1
        nums[j+1] = key

print(nums)


            

