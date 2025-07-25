# Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.
nums = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

max_len = 0

for i in range(len(nums)):
    current_sum = 0
    for j in range(i, len(nums)):
        current_sum += nums[j]
        if current_sum == k:
            max_len = max(max_len, j - i + 1)

print("Length of longest subarray:", max_len)

     
      
   
      




  
