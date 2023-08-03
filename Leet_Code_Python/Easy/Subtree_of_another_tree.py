'''
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


'''

class Solution:
    def isSubtree(
        self,
        root: Optional[TreeNode],
        subRoot: Optional[TreeNode]
    ) -> bool:
        def helper(node: Optional[TreeNode], subNode: Optional[TreeNode]):
            if node is None:
                return subNode is None
            if subNode is None:
                return (helper(node.left, subRoot) or
                helper(node.right, subRoot))
            if (node.val == subNode.val and
                helper(node.left, subNode.left) and
                helper(node.right, subNode.right)):
                return True
            elif (node.val == subRoot.val and
                helper(node.left, subRoot.left) and
                helper(node.right, subRoot.right)):
                return True
            return (helper(node.left, subRoot) or
                helper(node.right, subRoot))

        return helper(root, subRoot)
    

#less time

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self._isSubtree(root, subRoot)
    def _isSubtree(self, root, subRoot, started=False):
        return ((root is None) and (subRoot is None)) or \
            (
                    (root is not None) and (subRoot is not None) and ((
                        (root.val == subRoot.val) and
                        self._isSubtree(root.left, subRoot.left, True) and self._isSubtree(root.right, subRoot.right, True)
                    ) or (
                        not started and self._isSubtree(root.left, subRoot) or self._isSubtree(root.right, subRoot)
                    ))
            )
    
#less memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            stack = [(root1, root2)]
            while stack:
                n1, n2 = stack.pop()
                if n1.val != n2.val:
                    return False
                if bool(n1.left) ^ bool(n2.left):
                    return False
                if bool(n1.right) ^ bool(n2.right):
                    return False
                if n1.left:
                    stack.append((n1.left, n2.left))
                if n1.right:
                    stack.append((n1.right, n2.right))
            return True
                
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if isSame(node, subRoot):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
            
