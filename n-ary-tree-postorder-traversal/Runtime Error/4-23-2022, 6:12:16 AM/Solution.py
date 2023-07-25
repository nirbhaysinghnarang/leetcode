// https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        print(type(root))
        if not root.children:
            return [root.val]
        return self.postorder(root.children)+[root.val]