'''
closest binary tree value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

'''

def closestValue(root, target):
    closest = root.val

    while root:
        closest = min(root.val, closest, key=lambda x: abs(target - x))
        
        if target < root.val:
            root = root.left
        else:
            root = root.right

    return closest


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return float('inf')

        if root.val == target:
            return root.val
        elif root.val < target:
            rightRes = self.closestValue(root.right, target)
            return root.val if abs(root.val - target) < abs(rightRes - target) else rightRes
        elif root.val > target:
            leftRes = self.closestValue(root.left, target)
            return root.val if abs(root.val - target) < abs(leftRes - target) else leftRes