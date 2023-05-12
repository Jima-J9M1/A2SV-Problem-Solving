from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        incoming = defaultdict(int)
        queue = deque()
        sorted_order = []
        
        for index in range(len(alien_dict) - 1):
            min_val = min(len(alien_dict[index]), len(alien_dict[index + 1]))
            
            for i in range(min_val):
                if alien_dict[index][i] != alien_dict[index + 1][i]:
                    
                    graph[alien_dict[index][i]].append(alien_dict[index + 1][i])
                    incoming[alien_dict[index + 1][i]] += 1
                    break
        
    
        for i in range(K):
            if incoming[chr(i+97)] == 0:
                queue.append(chr(i+97))
                
        
                
        while queue:
            curr_letter = queue.popleft()
            sorted_order.append(curr_letter)
            
            for neighbor in graph[curr_letter]:
                incoming[neighbor] -= 1
                
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    
        
            
        return "".join(sorted_order)
