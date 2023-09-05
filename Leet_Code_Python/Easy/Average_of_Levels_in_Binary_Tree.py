'''
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        ans = []
        while q:
            qsize = len(q)
            sum_ = 0
            count = 0
            for _ in range(qsize):
                node = q.popleft()
                if node:
                    sum_ += node.val
                    count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(sum_/count)
        return ans


#less time

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = collections.deque()
        queue.appendleft(root)
        while queue:
            levelSum = 0
            nodesInLevel = len(queue)
            for i in range (nodesInLevel):
                node = queue.pop()
                levelSum += node.val
                if node.left: queue.appendleft(node.left)
                if node.right: queue.appendleft(node.right)
            ans.append(levelSum/nodesInLevel)
        return ans
    
#less memory

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        curr_level = [root]
        next_level = []
        curr_sum = 0 
        curr_len = len(curr_level)
        result = []

        while curr_level:
            node = curr_level.pop()
            curr_sum += node.val

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            
            if not curr_level:
                result.append(curr_sum / curr_len)
                curr_sum = 0
                curr_level, next_level = next_level, curr_level
                curr_len = len(curr_level)

        return result
    
    