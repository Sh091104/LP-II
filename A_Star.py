import heapq

def astar_tsp(graph, start):
    n = len(graph)
    frontier = []
    heapq.heappush(frontier, (0, [start], 0))
    min_path = None
    min_cost = float('inf')

    while frontier:
        f, path, cost_so_far = heapq.heappop(frontier)
        current = path[-1]

        if len(path) == n:
            total_cost = cost_so_far + graph[current][start]
            if total_cost < min_cost:
                min_cost = total_cost
                min_path = path + [start]
            continue

        for neighbor in range(n):
            if neighbor not in path:
                new_cost = cost_so_far + graph[current][neighbor]
                heapq.heappush(frontier, (new_cost, path + [neighbor], new_cost))

    return min_path, min_cost

# Get user input
n = int(input("Enter number of cities: "))
print("Enter the distance matrix row by row:")
graph = []
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    graph.append(row)

start = int(input("Enter the starting city (0 to {}): ".format(n - 1)))

path, cost = astar_tsp(graph, start)

print("Shortest TSP path:", path)
print("Total cost:", cost)


"""
Enter number of cities: 4  
Enter the distance matrix row by row:  
Row 1: 0 10 15 20  
Row 2: 10 0 35 25  
Row 3: 15 35 0 30  
Row 4: 20 25 30 0  
Enter the starting city (0 to 3): 0

"""