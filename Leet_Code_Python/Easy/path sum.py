'''Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.'''
def rootToLeafPathSum(self, root: TreeNode, targetSum: int, sum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            sum += root.val
            if sum == targetSum:
                return True   
        return self.rootToLeafPathSum(root.left, targetSum, sum + root.val) or self.rootToLeafPathSum(root.right, targetSum, sum + root.val)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        sum = 0
        return self.rootToLeafPathSum(root, targetSum, sum)

#less time
 def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def rc(node, pathSum):
            if not node:
                return False

            #print(f'Adding {node.val}')

            if not node.left and not node.right:
                return pathSum + node.val == targetSum

            return rc(node.left, pathSum + node.val) or rc(node.right, pathSum + node.val)

        return rc(root, 0)