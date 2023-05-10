class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        queue = deque(supplies)
        rec = []
        
        for indx in range(len(recipes)):
            for ingredient in ingredients[indx]:
                graph[ingredient].append(recipes[indx])
                degree[recipes[indx]] += 1
                
        
                
        while queue:
            node = queue.popleft()
            
            if node in degree:
                rec.append(node)
                
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                
                if degree[neighbor] == 0:
                    queue += [neighbor]
                    
        
                
        return rec