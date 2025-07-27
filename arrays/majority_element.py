# Given an integer array nums of size n, return the majority element of the array.
# The majority element of an array is an element that appears more than n/2 times in the array. The array is guaranteed to have a majority element.

#-------------brute force-----------------------------------------------------------------------------------

# nums = list(map(int,input("enter array elements:").split()))

# freq = {}

# for i in nums:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# for key,Value in freq.items():
#     if Value > len(nums)//2:
#         print(key)
          

#----------------------------optimal-----------------------------------------------------------------------
# Boyer-Moore Voting Algorithm.

nums = list(map(int,input("enter array elements:").split()))

count = 0
candidate = None

for num in nums:
    if count == 0:
        candidate = num
    if num == candidate:
        count+=1
    else:
        count-=1        

print(candidate)