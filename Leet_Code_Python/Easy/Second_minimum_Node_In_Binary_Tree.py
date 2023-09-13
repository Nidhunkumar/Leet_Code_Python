'''
671. Second Minimum Node In a Binary Tree
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

 

 

Example 1:


Input: root = [2,2,5,null,null,5,7]
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.
Example 2:


Input: root = [2,2,2]
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

'''
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            a.append(root.val)
            dfs(root.right)

        dfs(root)

        return (sorted(set(a)))[1] if len(set(a)) >= 2 else -1
    
#less time 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s=set()
        def helper(root,s):
            if(root==None):
                return 
            helper(root.left,s)
            s.add(root.val)
            helper(root.right,s)
        helper(root,s)
        s=list(s)
        s.sort()
        return s[1] if len(s)>1 else -1

#less memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        ans = -1
        def dfs(node, v):
            nonlocal ans

            if not node:
                return

            if node.val > v:
                if ans == -1:
                    ans = node.val
                else:
                    ans = min(ans, node.val)
                return

            dfs(node.left, v)
            dfs(node.right, v)

        dfs(root, root.val)
        return ans
