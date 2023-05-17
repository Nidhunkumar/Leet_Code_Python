'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, res = 0,0
        for num in nums:
            if count == 0:
                res = num
            
            if res == num:
                count = count + 1
            else:
                count = count - 1
                
        return res
    
#less time

class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    ans = None
    count = 0

    for num in nums:
      if count == 0:
        ans = num
      count += (1 if num == ans else -1)

    return ans
  
#less memory
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return max(set(nums),key = nums.count)
    