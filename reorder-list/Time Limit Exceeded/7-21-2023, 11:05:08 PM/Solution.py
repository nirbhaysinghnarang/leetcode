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
        newhead = head
        tmp = head


        second_half = self.mid(tmp)
        second_half=self.reverse(second_half)

        while second_half and newhead:
            newhead.next = second_half
            newhead = newhead.next
            second_half = second_half.next

        if second_half:
            newhead.next = second_half


        head = newhead
    

    def mid(self, head):
        fast, slow = head, head
        while(fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next

        return slow


    def reverse(self, head):
        prev, curr = None, head
        while curr is not None:
            nxt = curr.next
            prev = curr
            curr.next = prev
            curr = nxt

        return prev

