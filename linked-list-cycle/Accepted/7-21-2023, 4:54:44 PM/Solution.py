// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tmp = head
        visited = []
        while(tmp is not None):
            if tmp in visited:
                return True

            visited.append(tmp)
            tmp = tmp.next

        return False