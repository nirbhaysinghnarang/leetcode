// https://leetcode.com/problems/linked-list-cycle-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        f, s = head, head

        while(f and f.next):
            f = f.next.next
            s = s.next
            if (f==s):
                break

        if not f or not f.next:
            return -1

        s1 = head

        while(s!=s1):
            s1 = s1.next
            s = s.next

        return s