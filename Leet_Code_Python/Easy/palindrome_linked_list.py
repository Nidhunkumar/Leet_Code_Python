'''
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.


Example 1:
Input: head = [1,2,2,1]
Output: true


Example 2:
Input: head = [1,2]
Output: false
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True
#less time
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        
        fp=head
        mp=head
        p=None
        
        if not fp: return False
        if not fp.next: return True
        if not fp.next.next: return fp.val==fp.next.val
        
        while fp and fp.next:
            fp=fp.next.next
            
            mp.next,p,mp=p,mp,mp.next
            
        if fp:
            mp=mp.next
            
        while mp:
            
            if p.val!=mp.val:
                return False
            p=p.next
            mp=mp.next
        
        return True

#less memory
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None:
            return True
        slow=fast=head
        prev=None
        while fast.next and fast.next.next:
            fast=fast.next.next
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        if fast.next:
            curr=slow
        else:
            curr=prev
        slow.next,slow=prev,slow.next
        while slow!=None:
            if slow.val!=curr.val:
                return False
            slow=slow.next
            curr=curr.next
        return True

