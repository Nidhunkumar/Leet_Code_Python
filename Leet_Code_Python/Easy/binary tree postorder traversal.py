''' Binary Tree Postorder Traversal
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                stack.append(root.val)
        dfs(root)
        return stack
    

#less time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorder(root,ans):
    if root == None:
        return 
    postorder(root.left,ans)
    postorder(root.right,ans)
    ans.append(root.val)
    

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        postorder(root,ans)
        return ans

#less memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.val)
        return res