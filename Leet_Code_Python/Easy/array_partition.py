'''
561. Array Partition

Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example 1:

Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
Example 2:

Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5)
 + min(6, 6) = 1 + 2 + 6 = 9.

'''
nums = [6,2,6,5,1,2]
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([nums[-i * 2] for i in range(1,len(nums)//2 + 1)])

#less time
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum([n for i, n in enumerate(sorted(nums)) if i % 2 == 0])

#less memory

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        s = 0 
        nums.sort()
        ad = False
        while nums:
            mx = nums.pop()
            if ad:
                s += mx
            ad = not ad
        
        return s
        

