# Merge sort ante divide and conquer technique
def merge_sort(arr):
    # Oka element unte adi already sorted untadi, return cheyyali
    if len(arr) <= 1:
        return arr

    # Array ni madhya lo cut cheddham
    mid = len(arr) // 2

    # Left and right halves ni recursive ga sort cheyyadam
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Ippudu rendu sorted halves ni kalipi single sorted array cheyyali
    return merge(left_half, right_half)

# Merge function lo rendu sorted arrays ni kalipestham
def merge(left, right):
    sorted_arr = []  # Final sorted array ikkada store chestham
    i = j = 0  # i = left pointer, j = right pointer

    # Rendu arrays lo values compare cheyyadam
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            # Left value small unte adi add cheyyali
            sorted_arr.append(left[i])
            i += 1
        else:
            # Right value small unte adi add cheyyali
            sorted_arr.append(right[j])
            j += 1

    # Left lo inka migilina elements unte add cheyyali
    sorted_arr.extend(left[i:])
    # Right lo inka migilina elements unte kuda add cheyyali
    sorted_arr.extend(right[j:])

    # Final sorted array return chestham
    return sorted_arr

# Example
nums = [7, 4, 1, 5, 3]
sorted_nums = merge_sort(nums)
print("Sorted array:", sorted_nums)
