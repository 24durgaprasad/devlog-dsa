nums = list(map(int,input("enter array elements :").split()))
for i in range(len(nums)):
        if i not in nums:
                print(i)