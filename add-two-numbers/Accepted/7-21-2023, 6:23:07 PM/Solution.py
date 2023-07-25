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

        l1_new = []
        l2_new = []


        while(l1_rev):
            l1_new.append(str(l1_rev.val))
            l1_rev = l1_rev.next

        while(l2_rev):
            l2_new.append(str(l2_rev.val))
            l2_rev = l2_rev.next

        s = str(int("".join(l1_new)) + int("".join(l2_new)))[::-1]

        ret = ListNode(int(s[0]))
        curr = ret

        for i in range(1, len(s)):
            curr.next = ListNode(int(s[i]))
            curr = curr.next
        

        return ret


    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while(curr is not None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
