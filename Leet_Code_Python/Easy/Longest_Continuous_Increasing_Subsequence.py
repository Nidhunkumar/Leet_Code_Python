'''
674. Longest Continuous Increasing Subsequence
Given an unsorted array of integers nums, 
return the length of the longest continuous increasing subsequence (i.e. subarray).
 The subsequence must be strictly increasing.

A continuous increasing subsequence is defined 
by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

'''

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        counter=1
        temp=1
        for i in range(0,len(nums)-1):
            if nums[i]<nums[i+1]:
                temp+=1
                if temp>counter:
                    counter=temp
            else:
                temp=1
        return counter

#less time
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cu=0
        an=0
        for i in range(len(nums)):
            if i>0 and nums[i-1]>=nums[i]:
                an=i
            cu=max(i-an+1,cu)
        return cu
#less memory
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 0
        counter = 0

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                counter+=1
                if counter>=max_len:
                    max_len=counter
            else:
                counter=0

        return max_len+1
