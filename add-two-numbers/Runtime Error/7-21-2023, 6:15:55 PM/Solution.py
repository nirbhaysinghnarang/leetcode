// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = self.reverse(l1)
        l2_rev = self.reverse(l2)

        s = 0 

        while (l1_rev and l2_rev):
            s += (l1_rev.val + l2_rev.val)
            l1_rev = l1_rev.next
            l2_rev = l2_rev.next

        while(l1_rev):
            s+= l1_rev.val
            l1_rev = l1_rev.next

        while(l2_rev):
            s+= l2_rev.val
            l2_rev = l2_rev.next


        s = str(s)
        ret = ListNode(int(s[0]), None)
        for char in s[1:]:
            ret = ret.next
            ret.val = int(char)

        return ret


    def reverse(self, l):
        prev, curr = None, l

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            curr = curr.next
            prev = nxt

        return prev
