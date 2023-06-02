'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))
    
#less time
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        ans = set()
        for n in nums2:
            if n in set1:
                ans.add(n)
        return list(ans)

#less memory
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = []
        for i in nums1:
            for j in nums2:
                if i==j:
                    h.append(i)
        return set(h)