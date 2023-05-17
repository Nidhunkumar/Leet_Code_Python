'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:

 
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         # Initialize prev pointer as NULL...
        prev = None
        # Initialize the curr pointer as the head...
        curr = head
        # Run a loop till curr points to NULL...
        while curr:
            # Initialize next pointer as the next pointer of curr...
            next = curr.next
            # Now assign the prev pointer to curr’s next pointer.
            curr.next = prev
            # Assign curr to prev, next to curr...
            prev = curr
            curr = next
        return prev       # Return the prev pointer to get the reverse linked list... 
    
#less time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p, q = None, head
        while q:
            nxt = q.next
            q.next = p
            p, q = q, nxt
        return p
#less memory
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = []
        while head != None:
            ans.append(head.val)
            head = head.next
        ans = str(ans[::-1])
        ans = ans.replace("[" , "")
        ans = ans.replace("]" , "")
        ans = ans.replace(" " , "")
        return ListNode(ans)
