nums = list(map(int,input("enter array elements :").split()))
for i in range(len(nums)+1):
        if i not in nums:
                print(i)

        # optimal
        #         n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum