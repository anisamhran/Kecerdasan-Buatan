def find_all_paths(graph, start, goal, visited=[], path=[]):
    visited = visited + [start]
    path = path + [start]

    if start == goal:
        return [path]

    paths = []

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_paths = find_all_paths(graph, neighbor, goal, visited, path)
            for new_path in new_paths:
                paths.append(new_path)

    return paths

# Definisi graf yang merepresentasikan jarak antar kota
graph = {
    'A': ['C', 'F'],
    'B': ['E'],
    'C': ['A', 'D'],
    'D': ['C', 'E'],
    'E' : ['D', 'H', 'B'],
    'F' : ['A', 'G'],
    'G' : ['F', 'H'],
    'H' : ['G', 'E']
}

# State awal dan tujuan
start_state = 'A'
goal_state = 'B'

# Cari semua jalur dari state awal ke state tujuan
all_paths = find_all_paths(graph, start_state, goal_state)

# Tampilkan semua jalur yang ditemukan
print("Semua Alternatif Path:")
for i, path in enumerate(all_paths):
    print(f"Path {i+1}: {' -> '.join(path)}")

