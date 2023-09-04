# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        tmp = head
        visited = set()
        while(tmp is not None):
            if tmp in visited:
                return True

            visited.add(tmp)
            tmp = tmp.next

        return False