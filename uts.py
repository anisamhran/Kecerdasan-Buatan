from collections import deque

def rundfs(Source='A', target='T'):
    dfsresult = []
    visited = set()
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['A'], 'C': ['A', 'E'], 'D': ['A', 'E'], 'E': ['G', 'F', 'C', 'D'],
        'F': ['H', 'E','I','K'], 'G': ['I', 'E'], 'H': ['F', 'J', 'K'], 'I': ['F', 'K', 'L', 'G'], 'J': ['H', 'M'],
        'K': ['I', 'N', 'H'], 'L': ['N','I','S'], 'M': ['J', 'O'], 'N': ['K', 'L', 'O', 'Q'], 'O': ['N', 'M', 'R', 'P'],
        'P': ['O', 'T'], 'Q': ['R', 'N', 'S'], 'R': ['Q', 'T', 'O'], 'S': ['Q', 'L'], 'T': ['R', 'P']
    }
    
    def dfs(graph, visited, vertice):
        if vertice not in visited:
            dfsresult.append(vertice)
            visited.add(vertice)
            for neighbour in graph[vertice]:
                dfs(graph, visited, neighbour)
    
    if Source in graph:
        dfs(graph, visited, Source)
    return dfsresult


def runbfs(startnode='A', target='T'):
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['A'], 'C': ['A', 'E'], 'D': ['A', 'E'], 'E': ['G', 'F', 'C', 'D'],
        'F': ['H', 'E','I','K'], 'G': ['I', 'E'], 'H': ['F', 'J', 'K'], 'I': ['F', 'K', 'L', 'G'], 'J': ['H', 'M'],
        'K': ['I', 'N', 'H'], 'L': ['N','I','S'], 'M': ['J', 'O'], 'N': ['K', 'L', 'O', 'Q'], 'O': ['N', 'M', 'R', 'P'],
        'P': ['O', 'T'], 'Q': ['R', 'N', 'S'], 'R': ['Q', 'T', 'O'], 'S': ['Q', 'L'], 'T': ['R', 'P']
    }
    
    visited = set()
    queue = deque([startnode])
    result = []
    
    while queue:
        s = queue.popleft()
        if s not in result: 
            result.append(s)
        if s == target:
            break
        for adj in graph[s]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)
    
    return result

# Pemanggilan fungsi
bfsresult = runbfs('A', 'T')
print('Path with BFS', bfsresult)

print(' ')

dfsresult = rundfs('A', 'T')
print('Path with DFS', dfsresult)
