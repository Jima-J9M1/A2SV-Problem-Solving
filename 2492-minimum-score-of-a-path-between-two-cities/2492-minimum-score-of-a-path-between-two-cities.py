class Solution:
     def find(self,rep, size, x):
        parent = x
        
        while parent != rep[parent]:
            parent = rep[parent]
            
        while x != parent:
            root = rep[x]
            rep[x] = parent
            x = root
            
        return parent
    
     def union(self, rep, size, x, y):
        rep_x = self.find(rep, size, x)
        rep_y = self.find(rep, size, y)
        
        
        if rep_x == rep_y:
            return 
        
        
        if size[rep_x] > size[rep_y]:
            rep[rep_y] = rep_x
        elif size[rep_y] > size[rep_x]:
            rep[rep_x] = rep_y
        else:
            rep[rep_y] = rep_x
            size[rep_x] += 1
            
     def minScore(self, n: int, roads: List[List[int]]) -> int:
        # goal: return the minimum distance of road between cities.
        # roads list roads[i] = [ai, b1, distance ]
        # edge case if thery are not connected
        
        size = [1]*(n + 1)
        representatives = {i:i for i in range(1,n + 1)}
        
        
        for road in roads:
            self.union(representatives, size, road[0], road[1])
        
        connected_road = defaultdict(list)
        for i in range(1, n + 1):
            rep_road = self.find(representatives, size, i)
            representatives[i] = rep_road
        
        for road in roads:
            rep = representatives[road[0]]
            connected_road[rep].append(road[2])
        
        min_val = float("inf")
        for key in connected_road:
            if representatives[1] == key and representatives[n] == key:
                min_val = min(min_val, min(connected_road[key]))
                
        return min_val
        