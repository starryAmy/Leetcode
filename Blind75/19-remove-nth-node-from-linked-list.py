# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count nodes
        index = 0
        curr = head # otherwise you will move head
        while curr:
            index += 1
            curr = curr.next

        count = 0
        dummy = ListNode()
        prev = dummy
        prev.next = head
        while prev and prev.next:
            count += 1
            if count == (index - n + 1):
                temp = prev.next.next
                prev.next = temp
                prev = temp
                break
            prev = prev.next
        return dummy.next
