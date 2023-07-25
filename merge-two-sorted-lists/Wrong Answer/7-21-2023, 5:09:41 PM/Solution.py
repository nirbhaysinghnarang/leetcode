// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if not list1 and not list2:
            return []

        retList = ListNode()

        while(list1 is not None and list2 is not None):
            if list1.val <= list2.val:
                if not retList:
                    retList = list1
                else:
                    retList.next = list1
                list1 = list1.next
            else:
                if not retList:
                    retList = list2
                else:
                    retList.next = list2
                list2 = list2.next


        while(list2 is not None and list1 is None):
            if not retList:
                retList = list2
            else:
                retList.next = list2

            list2 = list2.next

        while(list1 is not None and list2 is None):
            if not retList:
                retList = list1
            else:
                retList.next = list1

            list1 = list1.next

        return retList

            



