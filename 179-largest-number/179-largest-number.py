class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        #concat two key and compare each other if greater and equal then return -1 else return 1         
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
        left = 0
        right = 0
        
        #Sort with insertion logic
        for index in range(1,len(nums)):
            
            right = index
            val = num_val[index]
            flag = sortingNum(num_val[right - 1], val)
            
            while right > 0 and flag == 1:
                num_val[right] = num_val[right - 1]
                right -= 1
                
                if right > 0:
                    flag = sortingNum(num_val[right - 1],val)
            
            num_val[right] = val
            
            
        return "".join(num_val)
                
            
            
        
        
        
#         num_val = [str(x) for x in nums]  
#         res = sorted(num_val, key=cmp_to_key(sortingNum))
        
#         return "".join(res)
                        
                
        
        