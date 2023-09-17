class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        end_mask = 0
        for i in range(len(graph)):
            end_mask += 1 << i
        
        ans = float('inf')

        for i in range(len(graph)):
            queue = collections.deque() 
            seen = set()
            queue.append([i, 1 << i])
            step = 0

            while queue:

                for _ in range(len(queue)):
                    cur_node, mask = queue.popleft()
                    if mask == end_mask:
                        queue = []
                        ans = min(ans, step)
                        break
                    if (cur_node, mask) in seen:
                        continue
                    seen.add((cur_node, mask))

                    for nxt in graph[cur_node]:
                        queue.append([nxt, mask | (1 << nxt)])
                
                step += 1
        return ans
            