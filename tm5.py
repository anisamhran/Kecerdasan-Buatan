def read_distances():
    """
    Reads the distances between cities from the user.
    """
    graph = {}
    num_cities = int(input("Enter the number of cities: "))  # Ask for the number of cities
    while True:
        edge = input("Enter edge between cities (format: 'from_city to_city distance', or type 'done' to finish): ").split()
        if edge[0] == 'done':
            break
        from_city, to_city, distance = edge
        if from_city not in graph:
            graph[from_city] = {}
        graph[from_city][to_city] = int(distance)
        if to_city not in graph:  # Ensure bidirectional edge
            graph[to_city] = {}
        graph[to_city][from_city] = int(distance)
    return graph

# Read the graph representing distances between cities from the user
graph = read_distances()


# Initial and goal states
start_state = input("Enter the start city: ")
goal_state = input("Enter the goal city: ")


def find_all_paths(graph, start, goal, visited=None, path=None, distance=0):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        return [(path[:], distance)]  # Copy path to avoid modifying the original path

    paths = []

    for neighbor, dist in graph[start].items():
        if neighbor not in visited:
            new_paths = find_all_paths(graph, neighbor, goal, visited.copy(), path.copy(), distance + dist)
            paths.extend(new_paths)

    return paths



# Find all paths from the initial state to the goal state
all_paths = find_all_paths(graph, start_state, goal_state)


# Display all found paths
print("All Alternative Paths:")
shortest_distance = float('inf')
shortest_path = None
for i, (path, total_distance) in enumerate(all_paths):
    path_str = ' -> '.join(path)
    print(f"Path {i+1}: {path_str} = Total distance: {total_distance}")

    if total_distance < shortest_distance:
        shortest_distance = total_distance
        shortest_path = path_str

# Display the shortest path
print("Shortest Path:", shortest_path)
print("Length of Shortest Path:", shortest_distance)





