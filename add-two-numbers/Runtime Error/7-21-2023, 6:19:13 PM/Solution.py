// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = self.reverseList(l1)
        l2_rev = self.reverseList(l2)
        print(l1_rev, l2_rev)

        l1_new = []
        l2_new = []


        while(l1_rev):
            l1_new.append(l1_rev.val)
            l1_rev = l1_rev.next

        while(l2_rev):
            l2_new.append(l2_rev.val)
            l2_rev = l2_rev.next

        print(l1_new, l2_new)
        ret = ListNode(int(s[0]), None)
        for char in s:
            ret = ret.next
            ret.val = int(char)

        return ret


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while(curr is not None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
