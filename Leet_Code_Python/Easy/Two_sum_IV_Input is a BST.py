'''
653. Two Sum IV - Input is a BST
Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.
Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false


'''

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:return False
        visit=set()
        q=[root]
        for i in q:
            if (k-i.val) in visit:return True
            visit.add(i.val)
            if i.left:
                q.append((i.left))
            if i.right:
                q.append(i.right)
        return False

           
#less time


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = set()
        def bfs(node):
            if not node:
                return False
            if k-node.val in vals:
                return True
            vals.add(node.val)
            return bfs(node.left) or bfs(node.right)
        
        return bfs(root)


#less memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.arr=[]
        self.dfs(root)
        comb=combinations(self.arr,2)
        for i in comb:
            if sum(i)==k: return True
        return False
    
    def dfs(self,root):
        if root is None: return
        self.arr.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited=[]
        queue=[root]
        while queue:
            node=queue.pop()
            findNum=k-node.val
            if findNum in visited: return True
            else: visited.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)
        return False


            