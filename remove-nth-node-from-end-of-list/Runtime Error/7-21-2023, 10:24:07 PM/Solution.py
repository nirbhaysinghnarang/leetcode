// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for i in range(n + 1):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next
            
