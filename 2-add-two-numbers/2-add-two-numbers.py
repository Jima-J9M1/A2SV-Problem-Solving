# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        Dummy = ListNode(0)
        size_1 = 0
        size_2 = 0
        left = l1
        right = l2
        
        while left:
            left = left.next
            size_1 += 1
        
        while right:
            right = right.next
            size_2 += 1
            
        
        carry = 0
        left = l1
        right = l2
        
        if size_2 >= size_1:
            Dummy.next = l2
            ptr = Dummy.next
            
            while right:
                
                if left:
                    cal = left.val + right.val + carry
                    carry = 0
                    
                    if cal > 9:
                        carry = cal // 10
                        cal = cal - 10
                    
                    ptr.val = cal
                   
                    left = left.next
                    
                    if right.next is None and carry > 0:
                        new_node = ListNode(carry,None)
                        right.next = new_node
                        ptr.next  = new_node
                        break
                        
                    ptr = ptr.next
                    right = right.next
                    continue
                    
                    
                cal = right.val + carry
                carry = 0
                if cal > 9:
                    carry = cal // 10
                    cal = cal - 10
                
                ptr.val = cal
                
            
                if right.next is None and carry > 0:
                    new_node = ListNode(carry,None)
                    right.next = new_node
                    ptr.next  = new_node
                    break
            
                ptr = ptr.next
                right = right.next
                
                
        else:
            
            
            Dummy.next = l1
            ptr = Dummy.next
            
            while left:
                
                if right:

                    cal = left.val + right.val + carry
                    carry = 0

                    if cal > 9:
                        carry = cal // 10
                        cal = cal - 10

                    ptr.val = cal
                    right = right.next
                    
                    
                    
                    if left.next is None and carry > 0:
                        new_node = ListNode(carry,None)
                        left.next = new_node
                        ptr.next  = new_node
                        break
                    ptr = ptr.next
                    left = left.next
                    continue


                cal = left.val + carry
                carry = 0
                if cal > 9:
                    carry = cal // 10
                    cal = cal - 10

                ptr.val = cal
                
                if left.next is None and carry > 0:
                        new_node = ListNode(carry,None)
                        left.next = new_node
                        ptr.next  = new_node
                        break
                        
                ptr = ptr.next
                left = left.next

        return Dummy.next
            
            
            