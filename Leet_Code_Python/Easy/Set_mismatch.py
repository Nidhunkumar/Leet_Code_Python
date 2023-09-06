'''
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]


'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        toRemove = sum(nums) - sum(set(nums))
        actualMissing = sum(range(1, len(nums)+1)) - sum(set(nums))
        return [toRemove, actualMissing]
    
#less time
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l_nums = len(nums)
        s_nums = sum(nums)
        ans = s_nums - sum(set(nums))
        return [ans, ans - ((s_nums) - ((l_nums+1) * l_nums // 2))]
    

#less memory
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        p=nums[0]
        j=1
        p=nums[0]
        miss=0
        nums.sort()
        for i in nums:
            if(nums.count(i)>1):
                p = i
                break
        for i in nums:
            if(j not in nums):
                miss = j
                break

            j+=1
        if(miss>p):
            return [p,miss]
        return [p,miss]

            
