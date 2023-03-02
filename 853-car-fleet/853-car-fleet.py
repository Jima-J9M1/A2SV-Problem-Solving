class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        time = [0] * len(position)
        
        for i in range(len(position)):
            position[i] = [position[i],speed[i]]
            
        position.sort(key=lambda x:x[0])
        
        for i in range(len(time)):
            time[i] = ( target - position[i][0] ) / position[i][1]
        
        
        stack = []
        for i in range(len(time)):
            
            # turn = False/
            
            while stack and stack[-1] <= time[i]:
                stack.pop()
                
            stack.append(time[i])
        
        
        return len(stack)
        
        