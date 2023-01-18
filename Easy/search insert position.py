'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''
if target not in nums:
            nums.append(target)
            nums[:]=sorted(nums)
            return nums.index(target)
        else:
            for  i in nums:
                if target == i:
                    return nums.index(i)


 
        left=0
        right=len(nums)-1
        #mid=(left+right)//2
        
        while left<=right:
            mid = (left+right) // 2
            if nums[mid]==target:
                return mid
            elif target <nums[mid]:
                right= mid-1
               
            elif target>nums[mid]:
                left=mid+1
                
        if nums[mid] > target:
            return mid
        else:
            return mid + 1



less memory
   if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
