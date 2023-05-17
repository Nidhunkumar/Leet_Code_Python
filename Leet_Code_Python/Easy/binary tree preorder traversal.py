'''
144. Binary Tree Preorder Traversal
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        preordered = []
        nodes = [root]
        
        while nodes:
            node = nodes[-1]
            del nodes [-1]
            
            if node.right is not None:
                nodes.append(node.right)
            
            if node.left is not None:
                nodes.append(node.left)
            
            preordered.append(node.val)

        return preordered

#less time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        head = root
        stack = []
        res = []

        while head or stack:
            if head:
                res.append(head.val)
                if head.right:
                    stack.append(head.right)
                head = head.left
            else:
                head = stack.pop()

        return res
                