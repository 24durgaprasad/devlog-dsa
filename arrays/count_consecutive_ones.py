def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
            
    max_count = max(max_count, current_count)        
    return max_count

nums = list(map(int,input("enter binary array values :").split()))
print(findMaxConsecutiveOnes(nums))