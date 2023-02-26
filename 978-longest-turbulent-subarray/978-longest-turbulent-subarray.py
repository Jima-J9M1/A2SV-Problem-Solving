class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        left = 0
        right = 0
        max_val = 0
        
        if len(arr) == 1:
            return 1
        
        while len(arr) > 1 and right < len(arr) - 1:
            
            if arr[right + 1] > arr[right]:
                if not stack:
                    stack.append(1)
                elif stack[-1] == 0:
                    stack.append(1)
                else:
                    
                    max_val = max(max_val,right - left + 1)
                    left = right 
                    stack = []
                    continue
                    
            elif arr[right + 1] < arr[right]:
                
                if not stack:
                    stack.append(0)
                elif stack and stack[-1] == 1:
                    stack.append(0)
                else:
                    max_val = max(max_val,right - left + 1)
                    left = right 
                    stack = []
                    continue
            else:
                max_val = max(max_val,right - left + 1)
                stack = []
                left  = right + 1
            
            right += 1
        
        max_val = max(max_val,right - left + 1)
        
        return max_val
                
            
        