# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev1 =None
        prev2 = None
        ptr1 = l1
        ptr2 = l2
        
        
        while ptr1:
            
            temp = ptr1.next
            ptr1.next = prev1
            prev1 = ptr1
            ptr1 = temp
            
        
        while ptr2:
            temp = ptr2.next
            ptr2.next = prev2
            prev2 = ptr2
            ptr2 = temp
            
        ptr1 = prev1
        ptr2 = prev2
        val1,val2,carry = 0,0,0
        Dummy = ListNode(0)
        ptr = Dummy

        while ptr1 or ptr2:
            val1,val2 = 0, 0
            if ptr1:
                val1 = ptr1.val
                ptr1 = ptr1.next
                
            if ptr2:
                val2 = ptr2.val
                ptr2 = ptr2.next
            
            cal = val2 + val1 + carry
            carry = 0
            if cal > 9:
                carry = 1
                cal %= 10

            new_node = ListNode(cal)
            ptr.next = new_node
            ptr = ptr.next
        
        if carry:
            new_node = ListNode(carry)
            ptr.next = new_node
            
            
        prev = None
        ptr = Dummy.next
        
        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
            
        return prev
            
                
                
            
            