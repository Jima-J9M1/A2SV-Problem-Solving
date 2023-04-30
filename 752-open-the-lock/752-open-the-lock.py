class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque(["0000"])
        visited = set()
        level = 0
        
        while queue:
            len_level = len(queue)
            
            for _ in range(len_level):
                
                code = queue.popleft()
                
                if code in deadends:
                    continue
                
                if code == target:
                    return level
                    
                for i in range(4):
                    
                    if code[i] == "0":
                        code1 = code[:i] + "1" + code[i + 1:]
                        code2 = code[:i] + "9" + code[i + 1:]
                        
                        if code1 not in visited:
                            queue.append(code1)
                            visited.add(code1)
                            
                        if code2 not in visited:
                            queue.append(code2)
                            visited.add(code2)
                        
                    else:
                        code3 = code[:i] + str(int(code[i]) + 1) + code[i + 1:]
                        code4 = code[:i] + str(int(code[i]) - 1) + code[i + 1:]
                        
                        if code3 not in visited and code[i] < "9":
                            queue.append(code3)
                            visited.add(code3)
  
                        if code4 not in visited:
                            queue.append(code4)
                            visited.add(code4)
                            
            level += 1
            
        return -1 