    import heapq
    def find(node,reps):
        if node != reps[node]:
            reps[node] = find(reps[node], reps)
        return reps[node]
    def union(node1,node2,reps,size):
        rep1 = find(node1, reps)
        rep2 = find(node2, reps)
        if rep1 == rep2:
            return 1
        if size[rep1] > size[rep2]:
            reps[rep2] = rep1
            size[rep1] += size[rep2]
        else:
            reps[rep1] = rep2
            size[rep2] += size[rep1]
        return 0
     
    def social(siz,edges):
        size = [1]*(siz)
        reps = {index:index for index in range(siz)}
        extras = 1
        for _ in range(edges):
            src, end = map(int,input().split())
            heap = []
            extras += union(src-1,end-1,reps,size)
            count = 0
            for key in reps:
                if key == reps[key]:
                    heapq.heappush(heap,-size[key])
            for _ in range(extras):
                count += -(heapq.heappop(heap))
            print(count-1)
                
     
    size,edges = map(int,input().split())
    social(size, edges)
