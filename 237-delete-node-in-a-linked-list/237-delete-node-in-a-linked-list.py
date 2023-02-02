# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
    
        node = None
        
        
    '''
    while node and node.next:
            node.val = node.next.val
            
            if node.next.next == None:
                node.next = None
                break
                
            node = node.next
      '''
        