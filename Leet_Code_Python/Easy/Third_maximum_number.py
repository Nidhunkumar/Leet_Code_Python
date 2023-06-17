'''
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<3:
            return max(nums)
        n=[-i for i in nums]
        heapq.heapify(n)
        for i in range(3):
            poping=heapq.heappop(n)
            if i==2:
                return -(poping)
            

#less time
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        dis = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            
            seen.add(num)
            dis += 1

            if dis == 3:
                return num
        
        return nums[0]

#less memory
import sys
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max1 = -2**31-1
        max2 = 0
        max3 = 0
        for num in nums:
            if max1 < num:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2 < num < max1 and num != max1:
                max3=max2
                max2=num
            elif max3 < num < max2 and num != max2:
                max3=num
        if max3 == -2**31-1 or max2 == -2**31-1:
            return max1
        return max3
