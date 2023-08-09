'''
589. N-ary Tree Preorder Traversal

Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]

'''

class Solution(object):
    def preorder(self, root):
        # To store the output result...
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        # Base case: If root is none...
        if root is None: return
        # Append the value of the root node to the output...
        output.append(root.val)
        # Recursively traverse each node in the children array...
        for child in root.children:
            self.traverse(child, output)

#less time

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        nums = [root.val]
        for child in root.children:
            nums += self.preorder(child)
        
        return nums
    
#less memory

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def order(node):
            if node is None:
                return []
            if node.children is None or len(node.children) == 0:
                return [node.val]
            else:
                val1 = []
                for child in node.children:
                    val1 += order(child)
                return [node.val] + val1
        
        return order(root)
    

    