# def nextPermutation(nums):
#     i = len(nums) - 2
#     while i >= 0 and nums[i] >= nums[i + 1]:
#         i -= 1

#     if i >= 0:
#         j = len(nums) - 1
#         while nums[j] <= nums[i]:
#             j -= 1
#         nums[i], nums[j] = nums[j], nums[i]

#     left, right = i + 1, len(nums) - 1
#     while left < right:
#         nums[left], nums[right] = nums[right], nums[left]
#         left += 1
#         right -= 1

# def generateAllPermutations(nums):
#     nums.sort()  # Start from the smallest permutation
#     first = nums[:]  # Save the starting point
#     print(nums[:])

#     while True:
#         nextPermutation(nums)
#         if nums == first:
#             break
#         print(nums[:])

# # Example:
# nums = [1, 2, 3]
# generateAllPermutations(nums)



def nextpermutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    nums[i+1:] = reversed(nums[i + 1:])

def allpermutations(nums):
    nums.sort()                # ✅ Fix 1: Call sort
    start = nums[:]            # ✅ Fix 2: Copy original list
    print(nums[:])             # First permutation

    while True:
        nextpermutation(nums)
        if nums == start:
            break
        print(nums[:])

# ✅ Fix 3: No wrong indentation
nums = [1, 2, 3]
allpermutations(nums)




   
     
    
        
