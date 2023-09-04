'''
628. Maximum Product of Three Numbers

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6


'''

class Solution:
    def maximumProduct(self, vec: List[int]) -> int:
        if len(vec) == 3:
            return vec[0] * vec[1] * vec[2]
        max1 = max2 = max3 = -1000 
        min1 = min2 = 1000
        for i in vec:
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
            if i < min1:
                min2 = min1
                min1 = i
            elif i < min2:
                min2 = i
        return max(max1 * max2 * max3, min1 * min2 * max1)
    
#less time

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = 1001
        min2 = 1001
        max1 = -1001
        max2 = -1001
        max3 = -1001
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num
            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num
        return max(max1 * max2 * max3, min2 * min1 * max1)
    
#less memory

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return max(nums[n - 1] * nums[n - 2] * nums[n - 3], nums[0] * nums[1] * nums[n - 1])
    
