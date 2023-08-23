# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # get the size of the linkedlist
        current = head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        remainder = count % k
        quotient = count // k
        current = head
        ans = []
        if quotient == 0:
            while current is not None:
                tmp = ListNode(current.val)
                ans.append(tmp)
                current = current.next
            difference = k - count
            for _ in range(difference):
                ans.append(None)
        else:
            for _ in range(k):
                new_head = ListNode(current.val)
                new_current = new_head
                current = current.next
                length = quotient + 1 if remainder > 0 else quotient
                for _ in range(length - 1):
                    new_current.next = ListNode(current.val)
                    new_current = new_current.next
                    current = current.next
                ans.append(new_head)
                remainder -= 1
        return ans
            