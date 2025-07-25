# Given an array of nums of n integers. Every integer in the array appears twice except one integer. Find the number that appeared once in the array.

nums = list(map(int,input("enter array elements : ").split()))
count = {}

for i in nums:
    if i in count:
        count[i]+=1
    else:
        count[i]=1    


for key, value in count.items():
    if value == 1:
        print("The number that appears once is:", key)
        break



# from collections import Counter

# nums = list(map(int, input("Enter array elements: ").split()))
# count = Counter(nums)

# for num in count:
#     if count[num] == 1:
#         print("The number that appears once is:", num)
#         break



# nums = list(map(int, input("Enter array elements: ").split()))
# result = 0

# for num in nums:
#     result ^= num

# print("The number that appears once is:", result)