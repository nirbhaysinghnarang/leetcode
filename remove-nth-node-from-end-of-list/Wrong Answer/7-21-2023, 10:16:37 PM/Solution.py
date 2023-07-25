// https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        rev=self.reverse(head)
        removed = self.removeNth(rev, n)
        return self.reverse(removed)


    def reverse(self, head):
        prev, curr = None, head


        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def removeNth(self, head, n):
        prev, tmp = None, head
        cnt = 1
        while(tmp is not None):
            cnt+=1
            prev = tmp
            tmp = tmp.next
            if cnt==n:
                prev.next = tmp.next

        return head
        
