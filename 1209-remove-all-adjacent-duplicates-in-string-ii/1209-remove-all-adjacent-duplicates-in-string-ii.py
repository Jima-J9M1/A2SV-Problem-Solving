class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #GIve: s, k(number of duplicated letters in s, they must be adjacent)
        #the answer is unique, which means no multiple answer
        #Return: string after the deletion of duplicate ch
        # s = abcd, k = 2 -> abcd
        # s = "deeedbbcccbdaa", k = 3 -> ddbbcccbdaa -> ddbbbdaa -> dddaa -> aa
        #                   i
        # stack = [[a,2]]
        # ans += stack[-1][1] * stacl[-1][0] 
        # time complexity: suppos N is the length of string O(N)
        # Space complexity: O(N)
        
        
        stack = []
        ans = ""
        
        for ch in s:
            if stack and stack[-1][0] == ch:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([ch, 1])
                
                
        for ele, freq in stack:
            ans += (freq * ele)
            
            
            
        return ans
                
                
        
        
        
        