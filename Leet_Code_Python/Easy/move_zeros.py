'''
283. Move Zeroes
Easy
13.6K
344
Companies
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i]==0:
                nums.append(0)
                nums.remove(0)

#less time
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insertIndex = 0
        length = len(nums)
        for i in range(length):
            if nums[i] != 0:
                nums[insertIndex] = nums[i]
                insertIndex+=1
        while insertIndex < length:
            nums[insertIndex] = 0
            insertIndex+=1

#less memory
#[0,1,0,3,12]
# 1 0
#[1,0,0,3,12]
#[1,3,0,0,12]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lp, rp, len_n = 0, 0, len(nums)
        while rp < len_n:
            while lp < len_n and nums[lp] != 0:
                lp += 1
                
            rp = lp + 1
            while rp < len_n and nums[rp] == 0:
                rp += 1
                
            if lp < len_n and rp < len_n and lp != rp:
                nums[lp], nums[rp] = nums[rp], nums[lp]
                lp += 1
        