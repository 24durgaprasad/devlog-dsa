def recursiveInsertionSort(nums, n=None):
    if n is None:
        n = len(nums)

    # Base case
    if n <= 1:
        return nums

    # Sort first n-1 elements
    recursiveInsertionSort(nums, n - 1)

    # Insert nth element into sorted array
    last = nums[n - 1]
    j = n - 2

    while j >= 0 and nums[j] > last:
        nums[j + 1] = nums[j]
        j -= 1

    nums[j + 1] = last

    return nums

# Example
nums = [2, 4, 5, 6, 1, 3]
print(recursiveInsertionSort(nums))
