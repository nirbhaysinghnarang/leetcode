// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head


        while(fast is not None):
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
            else:
                return slow
            slow = slow.next


        return slow
        
            



        