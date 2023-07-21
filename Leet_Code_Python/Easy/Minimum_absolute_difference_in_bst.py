'''

530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1

'''

class Solution:

    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.__get_minimum_diff(root, -maxsize, maxsize)

    @classmethod
    def __get_minimum_diff(cls, tree: TreeNode | None, lo: int, hi: int) -> int:
        if tree is None:
            return hi - lo
        return min(
            cls.__get_minimum_diff(tree.left, lo, tree.val),
            cls.__get_minimum_diff(tree.right, tree.val, hi),
        )
    
#less time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        listy = []
        def in_order(node):
            if node:
                in_order(node.left)
                listy.append(node.val)
                in_order(node.right)
        in_order(root)
        mad = float("inf")
        for i in range(len(listy)-1):
            mad = min(mad, abs(listy[i+1] - listy[i]))
        return mad

#less memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None  # Variable to track the previous node
        self.min_diff = float('inf')  # Initialize minimum difference with positive infinity
        self.inorder(root)  # Perform inorder traversal
        return self.min_diff
    
    def inorder(self, node):
        if node is None:
            return
        
        # Visit the left subtree
        self.inorder(node.left)
        
        # Check the difference with the previous node (if exists)
        if self.prev is not None:
            self.min_diff = min(self.min_diff, node.val - self.prev.val)
        
        self.prev = node  # Update the previous node
        
        # Visit the right subtree
        self.inorder(node.right)