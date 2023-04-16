from collections import defaultdict
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return input()
def LSI(): return list(input())
def LSI(): return [i for i in input().split()]

def dfs(node, graph, colors, color):
    colors[node] = color
    for child in graph[node]:
        if colors[child] == -1:
            if not dfs(child, graph, colors, 1 - color):
                return False
        elif colors[child] == color:
            return False
    
        
    return True

def main():
    node = II()
    if node == 0:
        return -1
    
    edge = II()
    graph = defaultdict(list)
    for __ in range(edge):
        v1, v2 = MI()
        graph[v1].append(v2)
        graph[v2].append(v1)


    colors = [-1] * (node + 1)

    for ele in graph:
        if colors[ele] == -1:
            if not dfs(ele, graph, colors, 0):
                return False
            
    return True

while True:
    ans = main()
    if ans == -1:
        break
    if ans:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
