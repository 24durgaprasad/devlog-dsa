# Given an array arr of n integers, where arr[i] represents price of the stock on the ith day. Determine the maximum profit achievable by buying and selling the stock at most once. 
# The stock should be purchased before selling it, and both actions cannot occur on the same day.
# print(max(nums)-min(nums))

nums = [10, 7, 5, 8, 11, 9]

min_price = nums[0]
max_profit = 0

for price in nums[1:]:
   if price < min_price:
      min_price = price                     
   else:
      profit = price - min_price
      max_profit = max(profit,max_profit)
    
print(max_profit)        