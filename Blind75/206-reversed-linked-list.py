# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr: # until there are no linked nodes
            temp = curr.next # stores the next value
            curr.next = prev # reverse the link
            prev = curr # current one becomes the previous one
            curr = temp # move to the next
        return prev
