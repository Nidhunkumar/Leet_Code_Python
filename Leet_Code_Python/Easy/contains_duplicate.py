'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
nums = [1,2,3,4]
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt={}
        if len(nums) <=0:
            return nums
        for i in nums:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i]=1 
        if max(cnt.values()) > 1:
           return True
        else:
            return False
        
#less time
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() 
        for n in nums: # iterating through list
            if n in hashset: #if number is already added to hashset
                return True #number is a duplicate
            hashset.add(n) #adding number to hashset
        return False #all numbers were added to set without matches
    
#less memory
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check=True
        nums.sort()
        for i in range(len(nums)-1):
            check=False
            nums[i] -= nums[i+1]

        if check:
            return False

        if nums.count(0) > 0 and nums[-1] != 0:
            return True
        else:
            return False

#less memory
'''
Brute force:
- use a hashmap to store frequencies
- if it appears twice, then return true. else, return false.
Time complexity: O(n)
Space complexity: O(n)

Or:
- sort, then use bisect (?)
- sorting takes O(n log n)
Time complexity: O(n log n)
Space complexity: O(1) - using inplace sort

Is it possible for space to be O(1)?
- binary
01 -> 1
10 -> 2
if I encounter 1 and 2, bit mask: 11
to check if a number is encountered, 1 << num | bitmask == 1
Python uses arbitrary length numbers, so space: O(n) bits -> however this will all be stored in a single number.

Another way: use input array as storage
how do I mark that something is visited?
- use "-1" to indicate that it's visited
- for 0, use some other value => maybe a is_zero_found value.

when i encounter the next value, how do I know if something is visited before?
- need to traverse through all elements before it to figure out if something is visited.

'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False


