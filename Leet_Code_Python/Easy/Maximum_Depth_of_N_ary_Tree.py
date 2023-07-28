'''
559. Maximum Depth of N-ary Tree


Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        
        return 1 + max_depth
    
#less time

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:

        def recursion(root, level):
            nonlocal res
            if not root.children:
                res = max(res, level)
                return
            for child in root.children:
                recursion(child, level + 1)
            return
        
        if not root:
            return 0

        res = 0
        recursion(root, 1)
        return res

#less memory

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        temp = [0]
        for c in root.children:
            temp.append(self.maxDepth(c))
        return max(temp)+1

