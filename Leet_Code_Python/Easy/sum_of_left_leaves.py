'''
404. Sum of Left Leaves

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0

'''

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # Define a helper function to recursively traverse the tree and compute the sum of left leaves
        def traverse(node, is_left):
            # If the current node is None, return 0
            if not node:
                return 0
            
            # If the current node is a leaf node and is a left child, return its value
            if not node.left and not node.right and is_left:
                return node.val
            
            # Recursively traverse the left and right subtrees
            left_sum = traverse(node.left, True)
            right_sum = traverse(node.right, False)
            
            return left_sum + right_sum
        
        # Call the helper function with the root node and False to indicate that the root is not a left child
        return traverse(root, False)
    
#less time

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0 
            
            left_sum = 0
            if root.left and not root.left.left and not root.left.right:
                left_sum = root.left.val
            return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        
#less memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [root]
        res = 0
        while stack:
            node = stack.pop(0)
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
