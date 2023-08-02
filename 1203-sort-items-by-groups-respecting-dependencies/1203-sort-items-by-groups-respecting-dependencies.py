class Solution:
    def topologicSort(self, nodes, graph, in_degree):
        queue = deque([node for node in nodes if node not in in_degree])
        ans = []
        
        while queue:
            item = queue.popleft()
            ans.append(item)
            
            for neighbor in graph[item]:
                in_degree[neighbor] -= 1
                
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
                    
                    
                    
        return ans
    
    
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        item_group = defaultdict(list)
        group_id = m
        
        for item in range(n):
            if group[item] == -1:
                group[item] = group_id
                group_id += 1
                
            item_group[group[item]].append(item)
            
        group_order_graph = defaultdict(list)
        item_indegree = defaultdict(int)
        
        for indx, items in enumerate(beforeItems):
            for item in items:
                if group[indx] == group[item]:
                    group_order_graph[item].append(indx)
                    item_indegree[indx] += 1
                    
        sorted_group_item = {}
        
        for item in item_group:
            sorted_item = self.topologicSort(item_group[item], group_order_graph, item_indegree)
            if len(sorted_item) != len(item_group[item]):
                return []
            
            sorted_group_item[item] = sorted_item
           
        grouped_graph = defaultdict(list)
        group_indegree = defaultdict(int)
        
        for indx, items in enumerate(beforeItems):
            for item in items:
                if group[indx] != group[item]:
                    grouped_graph[group[item]].append(group[indx])
                    group_indegree[group[indx]] += 1
                    
        groups = set(group)
        grouped_sorted_item = self.topologicSort(groups, grouped_graph, group_indegree)
        if len(groups) != len(grouped_sorted_item):
            return []
        
        ans = []
        for item in grouped_sorted_item:
            ans.extend(sorted_group_item[item])
        
        return ans
        
                    
                    
            
            
        
            
                    
    