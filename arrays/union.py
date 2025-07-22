num1 = list(map(int,input("enter first  array elements :").split()))
num2 = list(map(int,input("enter second array elements :").split()))

result = list(set(num1) | set(num2))
# result1 = list(set(num1).union(set(num2)))
# result3 = list(set(num1 + num2))

# # The apprach is pretty simple , we will be using set to remove dublicates so it is best way to get unique elements ,
# # then convert it to list or array 
# # | - set union operator it combines unique elements from both sets
# # .union - it is built in python function for union


print(result)


# other approach 

# num1 = [1, 2, 3, 4, 5]
# num2 = [1, 2, 3]

# union = []
# for num in num1 + num2:
#     if num not in union:
#         union.append(num)

# print(union)
