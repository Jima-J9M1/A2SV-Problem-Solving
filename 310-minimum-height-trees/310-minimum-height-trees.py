class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(set)
        
        
        for v1, v2 in edges:
            graph[v1].add(v2)
            graph[v2].add(v1)
            
        queue = deque([i for i in range(n) if len(graph[i]) == 1])

        while n > 2:
            length = len(queue)
            n -= length

            for _ in range(length):
                node = queue.popleft()
                child = graph[node].pop()
                graph[child].remove(node)

                if len(graph[child]) == 1:
                    queue.append(child)


        
        return list(queue)
        
        