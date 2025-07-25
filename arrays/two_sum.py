# nums = list(map(int,input("enter list elements:").split()))
# target = int(input("enter a number:"))

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(*sorted([i,j]))


#------------------------------------------------------------------------------------------------------------
# optimal
nums = list(map(int, input("Enter list elements: ").split()))
target = int(input("Enter the target number: "))

index_map = {}  # value -> index

for i, num in enumerate(nums):
    diff = target - num
    if diff in index_map:
        print(*sorted([i, index_map[diff]]))
        break
    index_map[num] = i
            

