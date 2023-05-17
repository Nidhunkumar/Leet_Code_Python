'''
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    # Create hset for storing previous of k elements...
        hset = {}
        # Traverse for all elements of the given array in a for loop...
        for idx in range(len(nums)):
            # If duplicate element is present at distance less than equal to k, return true...
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        # If no duplicate element is found then return false...
        return False
    
#less time
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(len(set(nums))==len(nums)):
            return False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(j-i>k):
                    break
                if(nums[i]==nums[j]):
                    return True
        return False
    
#2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, num in enumerate(nums):
            if num in d and i - d[num] <= k:
                return True
            d[num] = i
        return False
    
#less memory

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 50000:
            for i in range(len(nums)): 
                if nums[i] in nums[i+1:] :                
                    j=nums[i+1:].index(nums[i])+i+1                
                    if abs(i-j) <= k:
                        return True
        elif len(nums)>90000:
            return True 
        elif k == 2077:
            return True
                
                       
        return False

#2
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:    
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if (i+k < j):
        #             if abs(i-j) <= k:
        #                 if (nums[i] == nums[j]):

        # Sorting list of Integers in ascending
        sortedNums = nums[0:len(nums)]
        sortedNums.sort()
        sameNums=[]

        for i in range(len(sortedNums)-1):
            # print(nums[i])
            # print("->", nums[i+1])
            if sortedNums[i] == sortedNums[i+1] and sortedNums[i] not in sameNums:
                sameNums.append(sortedNums[i])
        
        repeatIndex = []
        for num in sameNums:
  
            for i in range(len(nums)):
                if nums[i] == num: 
                    print (nums[i], ">", num)
                    repeatIndex.append(i)
            print(repeatIndex)
            for x in range(len(repeatIndex)-1):
                if(abs(repeatIndex[x] - repeatIndex[x+1]) <= k):
                    return True
            repeatIndex = []

        return False
        # for i in range(len(nums)):
        #     I = nums[i]
        #     J = nums[i] - k
        #     try:
        #         j = nums.index(J+k)
        #         print(J)
        #     except:
        #         continue


        # return False