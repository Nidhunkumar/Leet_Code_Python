'''
83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

if not head:
            return None

        curr = head

        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

         temp=head
        while temp:
            while temp.next!=None and temp.val == temp.next.val:
                temp.next=temp.next.next
            temp=temp.next
        return head

#---------------
if not head or not head.next:
            return head
        prev=head
        ptr=head.next
        while(ptr):
            while(ptr and ptr.val==prev.val):
                ptr=ptr.next
            prev.next=ptr
            prev=ptr
            if ptr:
                ptr=ptr.next
        return head