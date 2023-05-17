'''
Missing Ranges
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
 def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
    def getRange(lo: int, hi: int) -> str:
      if lo == hi:
        return str(lo)
      return str(lo) + '->' + str(hi)

    if not nums:
      return [getRange(lower, upper)]

    ans = []

    if nums[0] > lower:
      ans.append(getRange(lower, nums[0] - 1))

    for prev, curr in zip(nums, nums[1:]):
      if curr > prev + 1:
        ans.append(getRange(prev + 1, curr - 1))

    if nums[-1] < upper:
      ans.append(getRange(nums[-1] + 1, upper))

    return ans