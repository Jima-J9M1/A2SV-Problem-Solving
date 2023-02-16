# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        _dict = defaultdict(int)
        
        while headA:
            _dict[headA] += 1
            headA = headA.next
            
        while headB:
            _dict[headB] += 1
            headB = headB.next
        
        node = 0
        for idx in (_dict):
            if _dict[idx] == 2:
                
                node = idx
                break
                
        
        return node if node else None