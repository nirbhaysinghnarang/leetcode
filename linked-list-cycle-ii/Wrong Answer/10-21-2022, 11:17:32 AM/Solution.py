// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head and not head.next:
            return False
        pointedTo = set()
        
        while head.next is not None:
            if head.next in pointedTo:
                return head.next
            pointedTo.add(head.next)
            head = head.next
        return None
        