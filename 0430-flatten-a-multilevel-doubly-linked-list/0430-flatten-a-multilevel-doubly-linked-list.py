"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Give: Dobule linked list -> prev, next, child
        #      child -> child, prev, next
        #Return: flatten(single-level-double-linkedlist), cur_node -> child -> cur_node.next
        
        
        
        def flattenSolution(cur, head):
            
            while cur:
                next = cur.next
                if cur.child:
                    new_node = flattenSolution(cur.child, cur.child)
                    cur.next = new_node
                    cur.child = None
                    new_node.prev = cur
                    
                    while cur.next:
                        cur = cur.next
                        
                    if next:
                        cur.next = next
                        next.prev = cur
                    
                cur =  next
                
            return head
        
        
        val = flattenSolution(head, head)
    
            
        return head
        