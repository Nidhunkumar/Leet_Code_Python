'''
448. Find All Numbers Disappeared in an Array
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

'''

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
       return set(range(1,len(nums)+1))-set(nums)

#less time

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(list(range(1, len(nums) + 1))).difference(nums)

#less memory
class Solution:
  def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    for num in nums:
      index = abs(num) - 1
      nums[index] = -abs(nums[index])

    return [i + 1 for i, num in enumerate(nums) if num > 0]
  