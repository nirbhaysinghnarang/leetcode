// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        mid = self.findMid(head)
        mid_rev = self.reverse(mid)
        s = 0


        while(head and mid_rev and head!=mid_rev):
            s = max(s, head.val+mid_rev.val)
            head = head.next
            mid_rev = mid_rev.next

        return s


    def findMid(self, head):
        f, s = head, head

        while(f and f.next):
            f = f.next.next
            s = s.next

        return s


    def reverse(self, head):
        prev, curr = None, head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


    