'''203. Remove Linked List Elements
Easy
7K
205
Companies
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:


Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
    
#less time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        slow = dummy
        fast = head
        while fast:
            if fast.val == val:
                slow.next = fast.next
            else:
                slow = slow.next
            fast = fast.next 
    
        return dummy.next
    
#less memory
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None 
        # if head.val==val:
        #     head=head.next
        root=head
        flag=0
        prev=head
        while root:
            while root and root.val==val:
                if root.next==None:
                    flag=1
                    root=root.next
                else:

                    root.val=root.next.val
                    root.next=root.next.next
            # print(root.val)
            if flag==1:
                prev.next=None
            prev=root
            if root: 
                root=root.next
        if head.val==val:
            head=head.next
        return head
            


