// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sz = 

        temp_head = head
        while(temp_head is not None):
            sz+=1
            temp_head = temp_head.next
        
        print(sz)
        temp_head = head
        target_idx = sz//2 if sz%2 else sz//2+1
        count = 0
        while(count!=target_idx):
            count+=1
            temp_head = temp_head.next

        return temp_head
        
            



        