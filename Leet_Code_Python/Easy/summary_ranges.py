'''
228. Summary Ranges

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

'''
class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    ans = []

    i = 0
    while i < len(nums):
      begin = nums[i]
      while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        i += 1
      end = nums[i]
      if begin == end:
        ans.append(str(begin))
      else:
        ans.append(str(begin) + "->" + str(end))
      i += 1

    return ans

#less time
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start, end, result = 0, 0, []
    
        while start < len(nums) and end<len(nums):
            if end+1 < len(nums) and nums[end]+1 == nums[end+1]:
                end=end+1
            else:
                if start == end:
                    result.append(str(nums[start]))
                    start = start + 1
                    end = end + 1
                else:
                    result.append(str(nums[start])+'->'+str(nums[end]))
                    start = end + 1
                    end = end + 1

        return result
#less memory
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums+=[2147483649];f=[];a='';v=False
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                if not v:
                    a=str(nums[i])+'-'+'>';v=True
            else :
                a+=str(nums[i])
                f.append(a)
                a='';v=False
        return f