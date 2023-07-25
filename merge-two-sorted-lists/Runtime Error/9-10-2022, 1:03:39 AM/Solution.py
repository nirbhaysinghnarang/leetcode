// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
         if l1 is None and l2 is None:
            return []
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if(l1.val<l2.val):
            tmp = head = ListNode(l1.val)
            l1 = l1.next
        else:
            tmp = head = ListNode(l2.val)
            l2 = l2.next
    
        while(l1 is not None and l2 is not None):
            if(l1.val<l2.val):
                tmp.next  = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        
        while(l1):
            tmp.next = ListNode(l1.val_
            l1 = (l1.next)
            tmp = tmp.next
            
        while(l2):
            tmp.next = ListNode(l2.val)
            l2 = l2.next
            tmp = tmp.next
                                
            
        
        return head
       