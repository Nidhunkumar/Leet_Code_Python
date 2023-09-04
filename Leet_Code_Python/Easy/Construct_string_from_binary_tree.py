'''
606. Construct String from Binary Tree

Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: root = [1,2,3,4]
Output: "1(2(4))(3)"
Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
Example 2:

Input: root = [1,2,3,null,4]
Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example, except we cannot omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def tree2str(self, root: Optional[TreeNode]) -> str:
                    
            if(root == None):
                return ""
            
            output: str = str(root.val)
            
            if (root.left != None or root.right != None):
                output += "(" + self.tree2str(root.left) + ")"
                
            if (root.right != None):
                output += "(" + self.tree2str(root.right) + ")"          
            
            return output;    

#less time 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node, arr):
            if not node:
                return
            if node:
                arr.append(str(node.val))
            if node.left:
                arr.append('(')
                dfs(node.left, arr)
                arr.append(')')
            if not node.left and node.right:
                arr.append('()')
            if node.right:
                arr.append('(')
                dfs(node.right, arr)
                arr.append(')')
        arr = []
        dfs(root, arr)
        return "".join(arr)
    
#less memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _tree2str(self, root: Optional[TreeNode]) -> str:
        return self.depth_first_pre_order(root)

    def depth_first_pre_order(self, node: Optional[TreeNode]) -> str:
        if not node.left and not node.right:
            return str(node.val)

        ans = ''
        ans += '(' + self.depth_first_pre_order(node.left) + ')' if node.left else '()'
        ans += '(' + self.depth_first_pre_order(node.right) + ')' if node.right else ''

        return str(node.val) + ans

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''

        stack = [root]
        ans = ''

        while stack:
            node = stack[-1]

            if hasattr(node, 'visited'):
                stack.pop()
                ans += ')'
            else:
                node.visited = True
                ans += '(' + str(node.val)

                if not node.left and node.right:
                    ans += '()'
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return ans[1:-1]
    
