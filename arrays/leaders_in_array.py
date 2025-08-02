# Given an integer array nums, return a list of all the leaders in the array.
# A leader in an array is an element whose value is strictly greater than all elements to its right in the given array. The rightmost element is always a leader. The elements in the leader array must appear in the order they appear in the nums array.


nums = [1, 2, 5, 3, 1, 2]

leader = nums[-1]
leaders = []
leaders.append(leader)
for i in nums[-2::-1]:
  if i > leader:
    leader = i
    leaders.append(i)

print(leaders[::-1])



  
