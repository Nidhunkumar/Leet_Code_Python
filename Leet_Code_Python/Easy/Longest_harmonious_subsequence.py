'''
594. Longest Harmonious Subsequence

We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.


Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0

'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        count_map = {}
        for num in nums:
            if num not in count_map:
                count_map[num] = 1
            else:
                count_map[num] += 1
        for num, count in count_map.items():
            if num + 1 in count_map:
                result = max(count + count_map[num + 1], result)
        return result
    
#less time

class Solution:
  def findLHS(self, nums: List[int]) -> int:
    counter = Counter(nums)
    m = 0

    for k, v in counter.items():
      if k + 1 in counter:
        m = max(m, v + counter[k + 1])
    
    return m
  

#less memory

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        max_len = 0
        for num in count:
            if num + 1 in count:
                max_len = max(max_len, count[num] + count[num + 1])
        
        return max_len

