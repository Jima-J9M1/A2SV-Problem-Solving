class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(len(quiet))]
        queue = deque()
        result = [0]*len(quiet)
        
        
        
        for edge in richer:
            v1, v2 = edge
            graph[v2].append(v1)
            incoming[v1] += 1    
        
        print(graph)
        for indx,ele in enumerate(incoming):
            if ele == 0:
                queue.append(indx)
                
        for indx in range(len(quiet)):
            colors = [0]*len(quiet)
            min_val = [float("+inf")]
            least_quiet = [-1]
            self.topSort(indx, graph, colors, min_val, least_quiet, quiet)
            result[indx] = least_quiet[0]
            
        return result
    
    
    def topSort(self,node, graph, colors, min_val, least_quiet, quiet):
        if colors[node] == 2:
            return
        
        if min_val[0] > quiet[node]:
            least_quiet[0] = node
            min_val[0] = quiet[node]
            
        colors[node] = 2
        for neighbor in graph[node]:
            self.topSort(neighbor, graph, colors, min_val, least_quiet, quiet)
            