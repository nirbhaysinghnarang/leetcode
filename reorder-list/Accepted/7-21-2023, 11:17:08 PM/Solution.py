// https://leetcode.com/problems/reorder-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None

        mid = self.mid(head)
        second_half = self.reverse(mid.next)
        mid.next = None

        self.mergeLists(head, second_half)
    

    def mid(self, head):
        fast, slow = head, head
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        return slow


    def reverse(self, head):
        prev, curr = None, head
        while(curr is not None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def mergeLists(self, head1, head2):
        while head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1
            head1, head2 = tmp1, tmp2
