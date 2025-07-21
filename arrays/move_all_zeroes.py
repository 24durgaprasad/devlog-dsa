# nums = list(map(int,input("enter array elements :").split()))
# #we take input from user


# # other way of taking input from user in array
# # nums = []
# # for _ in range(5):
# #     nums.append(int(input("enter number")))



# new_arr = []
# zeroes_count = 0

# # we create new array and trace count of zeroes

# for i in range(len(nums)): # iterate until the length of array so if size is 5 it iterates from 0 to 4
#     if nums[i] == 0:  # check if element in array is zero 
#         zeroes_count+=1 # increase count of zero
#     else:
#         new_arr.append(nums[i]) #else push element to new array

# for i in range(zeroes_count): # after pushing all non zero elements , trace the count of zeroes and push them at last
#     new_arr.append(0)            

# print(new_arr)    # print new array 

#-------------------------------------------------------------------------------------------------------------------

# optimal 

nums = list(map(int,input("enter array values :").split()))


non_zero_element = 0  # in this approach we will be swapping non zero elements so trace non zero index

for i in range(len(nums)):
    if nums[i] != 0: #if element is non zero
        nums[non_zero_element],nums[i] = nums[i],nums[non_zero_element] #swap it with non zero index to element
        non_zero_element+=1 # increase the non zero index 

print(nums)        