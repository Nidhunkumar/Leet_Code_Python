'''
590. N-ary Tree Postorder Traversal

Given the root of an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Example 2:


Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]

'''

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        arr = []
        def order(root):
            if root is None: return None
            for i in root.children:
                order(i)    
            arr.append(root.val)
        order(root)
        return arr
    
#less time

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        
        result = []
        stack = [root]
        prev = None
        
        while stack:
            node = stack[-1]
            
            if not node.children or prev == node.children[-1]:
                prev = stack.pop()
                result.append(prev.val)
            else:
                for child in node.children[::-1]:
                    stack.append(child)
            
        
        return result

#less memory

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        def dfs(node):
            if not node:
                return 


            out=[]

            for i in node.children:
                out.extend(dfs(i))


            out.append(node.val)

            return out

        return dfs(root)
