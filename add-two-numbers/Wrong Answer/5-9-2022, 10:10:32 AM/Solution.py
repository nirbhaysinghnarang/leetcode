// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        left = []
        
        while(l1):
            left.append(l1.val)
            l1 = l1.next
            
            
        right = []
        while(l2):
            right.append(l2.val)
            l2 = l2.next
            
            
        print(left, right)
        leftVal = 0
        rightVal = 0

        for i in range(len(left)):
            leftVal+=left[len(left)-1-i]*(10**(len(left)-1-i))
            
        for i in range(len(right)):
            rightVal+=right[len(right)-1-i]*(10**(len(right)-1-i))
            
        sumBoth = leftVal+rightVal
        return self.LLfromInt(sumBoth)
      
        
        
    def LLfromInt(self, i):
        if i>0:
            rNode = ListNode(i % 10)
            rNode.next = self.LLfromInt(i//10)
            return rNode
        return ListNode(0,None)
            
        
        
    
            