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
        print(head)
        cnt = 1
        while(tmp is not None):
            if cnt==n and prev:
                prev.next = tmp.next
            elif cnt==n:
                return head
            prev = tmp
            tmp = tmp.next
            cnt+=1
            


        return head
        
