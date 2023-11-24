class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for num in asteroids:
            while stack and stack[-1] > 0 and num < 0:
                
                if stack[-1] + num < 0:
                    stack.pop()
                    
                elif stack[-1] + num > 0:
                    break
                    
                else:
                    stack.pop()
                    break
            else: 
                stack.append(num)
                
        return stack
                    
                    