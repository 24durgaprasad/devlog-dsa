
def linear_search(nums,target):
 for i in range(len(nums)):
     if nums[i] == target:
         return i
    
 return -1
     
nums = list(map(int,input("enter elements :").split()))

target = int(input("enter target :"))     
     
x = linear_search(nums,target)     
print(x)