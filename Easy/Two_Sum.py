'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order

Examples:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
 ___
 |_|
 |_|
 
'''
nums=123 
i=nums%10
n=nums//10
print(n)


# lookup={
#      0:6,
#      1:2,
#      2:5,
#      3:5,
#      4:4,
#      5:5,
#      6:6,
#      7:3,
#      8:7,
#      9:6
# }
# result=0
# for i in nums:
#      result += lookup[i]
# print(result)
     
     





























nums=[1,2,4,7,8]
def twoSum(nums, target):
        hashMap ={nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in hashMap and hashMap[target-nums[i]] != i:
                return i, hashMap[target-nums[i]]


'''
code 3
time: O(n)
space:O(n)

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    numToIndex = {}

    for i, num in enumerate(nums):
      if target - num in numToIndex:
        return numToIndex[target - num], i
      numToIndex[num] = i
      
code 5

class Solution:
 def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

'''