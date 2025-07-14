# def quick_sort(arr):
#     # Base case: if array has 0 or 1 element, it's already sorted
#     if len(arr) <= 1:
#         return arr
    
#     # Choose a pivot (here we pick the last element)
#     pivot = arr[-1]
    
#     # Create 2 lists:
#     # 'less' will have all elements smaller than or equal to pivot
#     # 'greater' will have all elements greater than pivot
#     less = []
#     greater = []

#     for x in arr[:-1]:  # Exclude the pivot itself
#         if x <= pivot:
#             less.append(x)
#         else:
#             greater.append(x)
    
#     # Recursively sort both halves and combine them with the pivot
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# # Example
# nums = [7, 4, 1, 5, 3]
# sorted_nums = quick_sort(nums)
# print("Sorted:", sorted_nums)

def quick_sort_inplace(arr, low, high):
    if low < high:
        # Partition the array, and get the pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quick_sort_inplace(arr, low, pivot_index - 1)
        quick_sort_inplace(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Pick the last element as pivot
    i = low - 1        # Place for swapping

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]

    # Finally, place pivot in the correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Return pivot index

nums = [7, 4, 1, 5, 3]
quick_sort_inplace(nums, 0, len(nums) - 1)
print("Sorted:", nums)


#-------------------------------------------------------------------------------------------------------------------------
# def sort_nums(nums):
#   if len(nums) <= 1:
#     return nums
  
#   pivot = nums[0]
#   left = []
#   right = []

#   for i in nums[1:]:
#     if i <= pivot:
#       left.append(i)
#     else:
#       right.append(i)  
#   return sort_nums(left)+[pivot]+sort_nums(right)    





# nums = [3,4,1,6,2]
# sorted_nums = sort_nums(nums)
# print(sorted_nums)


# def quick_sort_in_place(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort_in_place(arr, low, pi - 1)
#         quick_sort_in_place(arr, pi + 1, high)

# def partition(arr, low, high):
#     pivot = arr[high]  
#     i = low - 1

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]

#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i + 1


# nums = [4,6,1,7,3]
# quick_sort_in_place(nums,0,len(nums)-1)
# print(nums)
