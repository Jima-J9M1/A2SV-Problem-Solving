class Solution:
    def find(self, city):
        if city == self.rep[city]:
            return city
        
        ret = self.find(self.rep[city])
        self.rep[city] = ret
        return ret
    
    
    def union(self, city1,city2):
        rep_city1 = self.find(city1)
        rep_city2 = self.find(city2)
        
        if rep_city1 != rep_city2:
            if self.size[rep_city1] > self.size[rep_city2]:
                self.rep[rep_city2] = rep_city1
                
            elif self.size[rep_city1] < self.rep[rep_city2]:
                self.rep[rep_city1] = rep_city2
                
            else:
                self.rep[rep_city1] = rep_city2
                self.size[rep_city2] += 1
                
                
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        length = len(isConnected)
        self.size = [0] * length
        self.rep = {i : i for i in range(length)}
        
        for indx, city in enumerate(isConnected):
            for i,ele in enumerate(city):
                if ele == 1:
                    self.union(indx,i)
        result = set()       
        for indx in range(len(isConnected)):
            result.add(self.find(indx))
            
        return len(result)
        
        
        
        
        
        
        '''
        graph = defaultdict(list)
        visited = set()
        count = 0
        
        
        def dfs(node):
            nonlocal graph
            nonlocal visited
            
            visited.add(node)
            

            for child in graph[node]:
                
                if child not in visited:
                    dfs(child)
                    
        for row in range(len(isConnected)):
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1:
                    graph[row + 1].append(col + 1)
                    
        for ele in graph:
            if ele not in visited:
                
                dfs(ele)
                count += 1

        
        return count
        
        '''
         
            
        
                    
