# Given an integer array nums of even length consisting of an equal number of positive and negative integers.Return the answer array in such a way that the given conditions are met:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
nums = [2, 4, 5, -1, -3, -4]

positives = []
negatives = []

# Step 1: Separate positives and negatives
for num in nums:
    if num > 0:
        positives.append(num)
    else:
        negatives.append(num)

# Step 2: Alternate them into a result array
result = []

for i in range(len(positives)):
    result.append(positives[i])
    result.append(negatives[i])

print(result)
