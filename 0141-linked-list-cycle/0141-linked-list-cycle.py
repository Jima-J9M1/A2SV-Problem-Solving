# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}
        if not head:
            return False
        
        while head.next and head.next not in dic:
            dic[head] = 1
            head = head.next
            
        if head.next in dic:
            return True
        
        return False
