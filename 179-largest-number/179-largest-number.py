class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def sortingNum(a,b):
            val_1 = a + b
            val_2 = b + a
            
            if val_1 >= val_2:
                return -1
            else:
                return 1
#             if len(a) == 1 and len(b) == b:
#                 if a > b:
#                     return -1
#                 elif a < b:
#                     return 1
#                 else:
#                     return 0
#             else:
                
#                 ptr1 = 0
#                 ptr2 = 0
                
                
#                 while ptr1 < len(a) and ptr2 < len(b):
#                     if a[ptr1] > b[ptr2]:
                        
#                         return -1
                    
#                     elif a[ptr1] < b[ptr2]:
                    
#                         return 1
#                     else:
#                         ptr1 += 1
#                         ptr2 += 1
                
#                 if ptr1 < len(a):
                    
#                     if int(a[ptr1]) == 0 or a[ptr1] < b[ptr2 - 1]:
#                         return 1
#                     else:
#                         return -1
                
#                 if ptr2 < len(b):
#                     if int(b[ptr2]) == 0 or a[ptr1 - 1] > b[ptr1]:
#                         return -1
#                     else:
#                         return 1
                    
        if sum(nums) == 0:
            return "0"
        
        num_val = [str(x) for x in nums]  
        res = sorted(num_val, key=cmp_to_key(sortingNum))
        
        return "".join(res)
                        
                
        
        