# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head.next and head.next.next == None:
            if head.val == head.next.val:
                return True
            else:
                return False
            
        elif head.next == None:
            return True
            

        slow = head
        fast = head.next.next
        length = head
        count = 0
        size = 0
        
        while length:
            length = length.next
            size += 1
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
            
        prev = None
        cur = head

        for _ in range(count + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        ptr = prev
        
        if size % 2 == 0: 
            slow = cur
        else:
            slow = cur.next
        

        while ptr and slow:

            if ptr.val != slow.val:
                return False
            
            ptr = ptr.next
            slow = slow.next
        
        
        return True

        