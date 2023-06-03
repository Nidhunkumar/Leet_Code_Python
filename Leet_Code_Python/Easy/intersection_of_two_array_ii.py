'''
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans
    
#less time
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
    
#less memory
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 <= len_nums2:
            for ele in nums1:
                if ele in nums2:
                    result.append(ele)
                    nums2.remove(ele)
            return result
        else:
            for ele in nums2:
                if ele in nums1:
                    result.append(ele)
                    nums1.remove(ele)
            return result
        
  
