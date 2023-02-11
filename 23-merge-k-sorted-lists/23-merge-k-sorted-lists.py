# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(0,None)
        ptr = head
        
        
        #Merge the nodes in the lists         
        for node in lists:
            ptr.next = node
            
            while ptr.next:
                ptr = ptr.next
        
        
        Dummy = ListNode(0)
        left = Dummy
        Dummy.next = head.next
        cur = head.next
        count = 1
        
        #Sort the the merged node
        
        while cur:
            
            ptr = left.next
            
            for i in range(count):
                if ptr.val > cur.val:
                    temp = cur.val
                    cur.val = ptr.val
                    ptr.val = temp
                    
                ptr = ptr.next
                
            
            count += 1
            cur = cur.next
            
        return Dummy.next
                
                
                    
            
            
            
            