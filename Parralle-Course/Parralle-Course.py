from collections import Counter, deque, defaultdict

def topoligicalSort(nodes, graph, in_degree):
    queue = deque([node for node in nodes if node not in in_degree])
    
    ans = []
    level = 0

    while queue:
        length = len(queue)

        for _ in range(length):
            cur_node = queue.popleft();
            ans.append(cur_node)

            for neighbor in graph[cur_node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        level += 1
    
    return ans,level

def parallelCourses(n, prerequisites):
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for c1,c2 in prerequisites:
        graph[c1].append(c2)
        in_degree[c2] += 1
    
    all_course = [course for course in range(1, n + 1)]
    
    sorted_course, semister = topoligicalSort(all_course, graph, in_degree)
    
    return semister if len(sorted_course) == len(all_course) else -1
        
