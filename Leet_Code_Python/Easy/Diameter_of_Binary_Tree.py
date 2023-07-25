'''
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1

'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def height(node=root):
            if not node:
                return 0
            if not node.left and not node.right:
                return 0
            chord = le = ri = 0
            if node.left:
                le = height(node.left)
                chord += 1 + le
            if node.right:
                ri = height(node.right)
                chord += 1 + ri
            self.diameter = max(chord, self.diameter)
            return 1+max(le, ri)
        height()
        return self.diameter
    
#less time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        def dfs(root):
            if not root:
                return -1#height of empty tree is -1
            #calculatre diameter
            left = dfs(root.left)#used to calculate the left and right height of node
            right = dfs(root.right)
            diameter[0] = max(diameter[0], left + right + 2)
            return 1 + max(left, right)#return the height of node
        dfs(root)
        return diameter[0]
        
#less memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.dfs(root, ans)
        return ans[0]

    def dfs(self, root: Optional[TreeNode], ans: List[int]) -> int:
        if not root:
            return 0
        left = self.dfs(root.left, ans)
        right = self.dfs(root.right, ans)
        ans[0] = max(ans[0], left + right)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        stack = [{'node': root, 'visited': False}]
        while stack:
            node_info = stack[-1]
            node = node_info['node']
            visited = node_info['visited']
            if visited:
                left = node.left.diameter if node.left else 0
                right = node.right.diameter if node.right else 0
                ans = max(ans, left + right)
                node.diameter = max(left, right) + 1
                stack.pop()
            else:
                node_info['visited'] = True
                if node.left:
                    stack.append({'node': node.left, 'visited': False})
                if node.right:
                    stack.append({'node': node.right, 'visited': False})
        return ans

