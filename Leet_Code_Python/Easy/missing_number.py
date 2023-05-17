'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        expectedSum = int(n*(n+1)/2)
        sum= 0
        for num in nums:
            sum = sum + num
        missingNumber = expectedSum-sum
        return missingNumber

#less time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arraySum = sum(nums)
        
        actualSum = (len(nums) * (len(nums) + 1)) // 2
        
        return actualSum - arraySum

#less memory
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # when good turn -1 or None
        for i in range(len(nums)):
            if nums[i] != -1:
                next_i = nums[i]
                while next_i < len(nums) and next_i != -1:
                    next_next_i = nums[next_i]
                    nums[next_i] = -1
                    next_i = next_next_i

        for i in range(len(nums)):
            if nums[i] > -1:
                return i
        return len(nums)