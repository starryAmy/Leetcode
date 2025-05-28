class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle one using fast/slow pointers:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None # separate the first half from the second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
