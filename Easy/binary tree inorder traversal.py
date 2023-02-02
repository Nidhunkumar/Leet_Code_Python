'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
'''

  stack = []
        def traverse(root):
            #base condition
            if root is None:
                return None
             #visit left tree
            traverse(root.left)
            #visit base node
            stack.append(root.val)
            # visit right node
            traverse(root.right)
        traverse(root)

#less time

        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right
        return res