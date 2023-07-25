// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return False
        
        pointedTo = set()
        while head is not None:
            if head in pointedTo:
                return True
            pointedTo.add(head)
            head = head.next
        
        return False
        