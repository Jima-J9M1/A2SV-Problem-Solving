class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safeState = defaultdict(list)
        incoming = [0]*len(graph)
        
        for indx,node in enumerate(graph):
            for ele in node:
                safeState[indx].append(ele)
                incoming[ele] += 1
                
                
        safe_node = []
        
        
        colors = [0] *len(graph)
        for state in range(len(graph)):
            
            cycle_found = self.hasCycle(state, graph,colors, safe_node)

        safe_node.sort()
        return safe_node
        
        
    def hasCycle(self, node, graph, colors, safe_node):
        if colors[node] == 2:
            return False
        
        if colors[node] == 1:
            return True
        
        colors[node] = 1

        for neighbor in graph[node]:
            has_cycle = self.hasCycle(neighbor, graph, colors, safe_node)
            
            if has_cycle:
                return True
            
        colors[node] = 2
        safe_node.append(node)
        
        return False
                