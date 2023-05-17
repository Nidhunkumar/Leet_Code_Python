'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        total_nums = len(nums)
        if not total_nums:
            return None
        mid_node = total_nums // 2
        return TreeNode(nums[mid_node],self.sortedArrayToBST(nums[:mid_node]), self.sortedArrayToBST(nums[mid_node + 1 :]))
    
    #less time
    class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        size = len(nums)
        #if size == 1:
        #    return nums[size-1]

        def convert(left, right):
            if left > right:
                return None
            mid = (left + right) // 2

            # process left
            left = convert(left, mid - 1)
            node = TreeNode(nums[mid])
            node.left = left
            node.right = convert(mid+1, right)
            return node
        return convert(0, size-1)