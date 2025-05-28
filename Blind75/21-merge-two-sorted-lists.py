# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # set up a new linked list
        dummy = ListNode()
        node = dummy
        while list1 and list2:
            if list1.val > list2.val:
                node.next = list2
                list2 = list2.next # move to the next one
            else:
                node.next = list1
                list1 = list1.next
            node = node.next
        if list1:
            node.next = list1
        else:
            node.next = list2
        return dummy.next # dummy is a linked list with a dummy variable at the beginning
