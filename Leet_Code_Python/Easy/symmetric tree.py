'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
'''
 if leftRoot is None and rightRoot is None:
            return True
        if (leftRoot is None and rightRoot is not None) or (leftRoot is not None and rightRoot is None):
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)
    def isSymmetric(self, root):
        return self.isTreeSymmetric(root.left, root.right)


         #inner function
        def compareSides( left, right):
            #base case
            if left is None and right is None:
                return True
            #if left and right both value exists and equal
            elif left and right and (left.val == right.val) :
                # recursively call compareSides function for left and right side
                return   compareSides(left.left, right.right) and compareSides(left.right, right.left)
                 
            # otherwise return false
            else:
                return False           
    
        return compareSides(root.left, root.right)