# Given an array nums of n integers.
# Return the length of the longest sequence of consecutive integers. The integers in this sequence can appear in any order.


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
num_set = set(nums)
longest = 0

for n in num_set:
    if n - 1 not in num_set:  # is this the start of a sequence?
        length = 1
        while n + length in num_set:
            length += 1
        longest = max(longest, length)

print(longest)

