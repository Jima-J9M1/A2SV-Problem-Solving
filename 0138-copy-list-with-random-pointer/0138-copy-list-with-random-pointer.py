"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        
        cur = head
        _dict = {}
        prev = None
        
        while cur:
            _dict[cur] = copy.copy(cur)
            
            if prev:
                _dict[prev].next = _dict[cur]
                
            prev = cur
            cur = cur.next
        
        cur = head
        
        while cur:
            if cur.random:
                _dict[cur].random = _dict[cur.random]
                
            cur = cur.next
        
        return _dict[head]
        
        
        
        