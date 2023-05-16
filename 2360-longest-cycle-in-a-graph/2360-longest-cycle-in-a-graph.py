class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        colors = [0]*len(edges)
        
        for indx, ele in enumerate(edges):
            if ele != -1:
                graph[indx].append(ele)
        
        long_cycle = 0
        
        for indx in range(len(edges)):
            longest_cycle = [0]
            count_node = defaultdict(int)
            self.hasCycle(indx,count_node, graph, colors, longest_cycle, 0)
            long_cycle = max(long_cycle, longest_cycle[0])
            
        return long_cycle if long_cycle > 0 else -1
                
                
    def hasCycle(self,node, count_node,graph, colors, longest_cycle, cycle):
        if colors[node] == 2:
            return
        
        if colors[node] == 1:
            longest_cycle[0] = max(longest_cycle[0], cycle - count_node[node])
            return
        
        colors[node] = 1
        
        for child in graph[node]:
            if colors[child] == 0:
                count_node[child] += count_node[node] + 1
                self.hasCycle(child, count_node, graph, colors, longest_cycle, cycle + 1)
                
            else:
                self.hasCycle(child, count_node, graph, colors, longest_cycle, cycle + 1)

            
            
        colors[node] = 2
        return 
            