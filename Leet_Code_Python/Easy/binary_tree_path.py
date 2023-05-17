'''
257. Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
Example 2:

Input: root = [1]
Output: ["1"]
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add(self, value):
        node = Node(value)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.length += 1

    def remove_first(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value

class Queue:
    def __init__(self, size = 0):
        self.list = LinkedList()
        self.size = size

    def enqueue(self, value):
        self.list.add(value)

    def dequeue(self):
        return self.list.remove_first()
    
    def is_empty(self):
        return self.list.head == None

class Solution:
    def binaryTreePaths(self, rootNode: Optional[TreeNode]) -> List[str]:
        if not rootNode:
            return
        else:
            queue = Queue()
            queue.enqueue(rootNode)
            paths = {
                f"0-{rootNode.val}": str(rootNode.val)
            }
            next_counter = 0
            current_counter = 0
            while not queue.is_empty():
                current = queue.dequeue()
                current_parent = paths[f"{current_counter}-{current.val}"]
                if current.left:
                    next_counter += 1
                    paths[f'{next_counter}-{current.left.val}'] = f'{current_parent}->{current.left.val}'
                    queue.enqueue(current.left)
                if current.right:
                    next_counter += 1
                    paths[f'{next_counter}-{current.right.val}'] = f'{current_parent}->{current.right.val}'
                    queue.enqueue(current.right)
                if current.right or current.left:    
                    del paths[f"{current_counter}-{current.val}"]
                current_counter += 1
            return list(paths.values())
        
#less time
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        return [str(root.val) + '->' + path for path in left + right]
    
#less memory
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return list(self.generate(root))

    def generate(self, root: TreeNode) -> Iterator[str]:
        stack = [root]
        paths = [[root.val]]

        while stack:
            node = stack.pop()
            path = paths.pop()

            if not node.left and not node.right:
                yield "->".join(str(x) for x in path)

            if node.left:
                stack.append(node.left)
                paths.append(path + [node.left.val])

            if node.right:
                stack.append(node.right)
                paths.append(path + [node.right.val])