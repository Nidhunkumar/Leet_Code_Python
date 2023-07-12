'''
501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]

'''
class Solution:
    def findMode(self, root: TreeNode) -> list[int]:

        def dfs(root: TreeNode)-> None:
            if not root: return

            d[root.val]+=1

            dfs(root.left)
            dfs(root.right)

            return

            
        d, ans = defaultdict(int), []
        
        dfs(root)
        mx = max(d.values())

        return [key for key in d if d[key] == mx]
    
#less time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        from collections import Counter
        path = []
        self.traverse(root, path)
        count = Counter(path)
        max_freq = max(count.values())

        return [num for num, freq in count.items() if freq == max_freq]


    def traverse(self, root, path):
        if not root:
            return

        self.traverse(root.left, path)
        path.append(root.val)
        self.traverse(root.right, path)
        
#less memory
from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inorder(root):
            if not root:
                return 
            root.left=inorder(root.left)
            res.append(root.val)
            root.right=inorder(root.right)
        inorder(root)
        x=Counter(res)
        maxi=max(x.values())
        ans=[]
        for k,v in x.items():
            if v==maxi:
                ans.append(k)
        return ans
    
