'''
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2


'''
nums= [1,1,0,1,1,1]
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:


        return max([len(i) for i in (''.join([str(i) for i in nums])).split("0")])

        
#less time

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num = 0
        num1 = 0
        for i in nums:
            if i == 0:
                if num1 > num:
                    num, num1 = num1, 0
                else:
                    num1 = 0
            else:
                num1 += 1

        return num if num > num1 else num1

#less memory
    
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_count = 0
        max_count = 0
        
        for i in nums:
            if i == 1:
                current_count += 1
                max_count = max(max_count, current_count)
                
            else:
                current_count = 0
        return max_count 
