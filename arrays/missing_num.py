nums = list(map(int,input("enter array elements :").split()))
for i in range(len(nums)+1):
        if i not in nums:
                print(i)