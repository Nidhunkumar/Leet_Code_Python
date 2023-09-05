'''
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000

'''

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = sum(nums[:k])
        maxAverage = windowSum/k
        for i in range(len(nums)-k):
            windowSum = windowSum-nums[i]+nums[i+k]
            maxAverage = max(maxAverage, windowSum/k)
        return maxAverage
    
#less time

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxavg = curavg = sum(nums[:k])
        for i in range(len(nums) - k):
            curavg += nums[i+k] 
            curavg -= nums[i]
            if curavg > maxavg:
                maxavg = curavg
        return maxavg / k
    
#less memory

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[:k])
        now = res
        for i in range(k, len(nums)):
            now += nums[i] - nums[i - k]
            res = max(res, now)

        nums.clear()
        del now
        return res / k

