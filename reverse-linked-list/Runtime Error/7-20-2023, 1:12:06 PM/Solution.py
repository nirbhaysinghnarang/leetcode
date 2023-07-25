// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return []

        if head.next is None:
            return head

        tmp_head = head
        head = head.next
        head.next = tmp_head

        return self.reverseList(head.next.next)