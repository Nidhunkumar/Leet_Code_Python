'''Given a binary tree, determine if it is 
height-balanced
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
           return (self.Height(root) >= 0)
    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1
    
#less time
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def sample(root):
            if not root:
                return 0
            lh = sample(root.left)
            if lh == -1:
                return -1
            rh = sample(root.right)
            if rh == -1:
                return -1
            if abs(lh-rh)>1:
                return -1
            else: 
                return 1+max(lh,rh)
            
        return sample(root)!=-1