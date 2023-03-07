class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        len_arr = len(arr)
        
        for i in range(len(arr)):
            #Loop through the element of arr if the last element of the stack is greater than the current one will pop and calculate
            # before ( subarray element that is greater than the last element of the stack) and after(subarray element that is greater than the last element of the stack) add it the ans
            
            while stack and arr[stack[-1]] > arr[i]:
                temp = stack.pop()
                after = i - temp
                before = 0
                
                #check if the stack is empty after the last index popped and if the stack is empty add it to one on the result    
                if not stack:
                    before = temp + 1
                else:
                    before = temp - stack[-1]
                    
                
                ans += before*after*arr[temp]
                
            stack.append(i)
            
        #after the above oppeation if the stack is not empty calculate the operation until the stack is empty
        while stack:
            temp = stack.pop()
            after = len(arr) - temp
            before = 0
            
            if not stack:
                before = temp + 1
                
            else:
                before  = temp - stack[-1]
            
            ans += before * after * arr[temp]
        return ans % (10**9 + 7)
                
                