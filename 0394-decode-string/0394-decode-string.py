class Solution:
    def decodeString(self, s: str) -> str:
        #give: encode str -> num, str, square bracket
        #return: to decode the string
        
        # 1. s = "3[a]2[bc]"
        #      3*("a") + 2*(bc)
        #      aaa + bcbc = aaabcbc
        
        # 2.  s = 3[a2[c]]
        #     3*(a2[c])
        #     3*(a + 2*(c))
        #     3 * (a + cc) = 3 * (acc)
        #     accaccacc
        
        
        #1.edge case, when there is one value
        #2.edge case
        
        #Approach
        #Define function decode, accept string paramter
        #Create a variable ans to store decoded string
        #Loop through the encoded string and until we find the number we will concat the character in variable ans
        #When we found the number, iterate strating from the opening square bracket to the clossing square bracket.
        #Call the function decode with the parameter new string from starting square to clossing square bracket multiply the function by the number we found in step 4 and concat with the ans variable, and we repeat the step from 3rd steps.
        #if we reach the end of the string we return the ans variable.
        
        
        
        stack = []
        curNum = 0
        curString = ""
        
        for ch in s:
            if ch == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ""
                curNum = 0
                
            elif ch == ']':
                prevNum = stack.pop()
                prevString = stack.pop()
                curString = prevString + prevNum*curString
            elif ch.isdigit():
                
                curNum = curNum*10 + int(ch)
                
            else:
                curString += ch
                
        
        return curString
    
    
#         def decode(s):
#             ans = ""
#             i = 0
            
#             while i < len(s):
#                 if not s[i].isdigit():
#                     ans += s[i]
#                     # print(s[i])
                    
#                 else:
#                     # print(s[i])
#                     #after we found the number we garuante that the next character is square bracket
#                     digit = s[i]
#                     i += 1
#                     while s[i].isdigit():
#                         digit += s[i]
#                         i += 1
                        
#                     i += 1
#                     digit = int(digit)
#                     square_brac = 1
                    
                    
#                     start = i
                    
#                     while i < len(s) and square_brac != 0:
#                         if s[i] == '[':
#                             square_brac += 1
                            
#                         if s[i] == ']':
#                             square_brac -= 1
                            
#                         i += 1
                        
#                     ans += (digit * decode( s[start:i - 1]))
                    
#                     continue
                    
                    
#                 i += 1
                
                
#             return ans
            
#         res = decode(s)
            
#         return res
        
        
                        
                    
                            
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        