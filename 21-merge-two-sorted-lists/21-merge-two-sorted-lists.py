# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(node1,node2,Dummy):
            
            if node1 == None and node2 == None:
                return 
            
            if node1 == None and node2 != None:
                return node2
            
            if node1 != None and node2 == None:
                return node1
            
            if node1.val <= node2.val:
                new_node = ListNode(node1.val)
                Dummy.next = new_node
                new_node.next = merge(node1.next,node2,Dummy.next)
                return new_node
            
            else:
                new_node = ListNode(node2.val)
                Dummy.next = new_node
                new_node.next = merge(node1,node2.next, Dummy.next) 
                return new_node
            
            
        Dummy = ListNode(0)
        val = merge(list1, list2,Dummy)
        return val
        