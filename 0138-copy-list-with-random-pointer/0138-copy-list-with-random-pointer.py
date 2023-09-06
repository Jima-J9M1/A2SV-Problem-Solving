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
        #goal: return the head of the copied linked list
        #approach: hash the original to the copied one
        #        : the link the copied to the next new node
        #        : after that from from the begining link the node and with their random
        if not head:
            return 
        
        cur = head
        hashmap = dict()
        prev = None
        while cur:
            hashmap[cur] = copy.copy(cur)
            
            if prev:
                hashmap[prev].next = hashmap[cur]
                
            prev = cur
            cur = cur.next
            
        cur = head
        
        while cur:
            if cur.random:
                hashmap[cur].random = hashmap[cur.random]
            
            cur = cur.next
            
        return hashmap[head]
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            