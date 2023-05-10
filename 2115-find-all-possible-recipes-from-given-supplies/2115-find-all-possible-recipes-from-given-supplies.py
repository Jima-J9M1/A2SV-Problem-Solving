class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        queue = deque()
        rec = []
        
        for indx in range(len(recipes)):
            for ingredient in ingredients[indx]:
                graph[ingredient].append(recipes[indx])
                degree[recipes[indx]] += 1
                
        for ele in supplies:
            degree[ele] += 0
                
        for key in degree:
            if degree[key] == 0:
                queue += [key]
                
        while queue:
            node = queue.popleft()
            
            if node in recipes:
                rec.append(node)
                
            for neighbor in graph[node]:
                degree[neighbor] -= 1
                
                if degree[neighbor] == 0:
                    queue += [neighbor]
                    
        
                
        return rec