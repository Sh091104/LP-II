import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.G = nx.Graph()  # For visualization

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.G.add_edge(u, v)  # Add to visualization graph

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def visualize(self):
        pos = nx.spring_layout(self.G)
        nx.draw(self.G, pos, with_labels=True, node_color='skyblue', node_size=1200, font_size=14, font_weight='bold')
        plt.title("Graph Visualization (Undirected)", fontsize=16)
        plt.show()

# Create graph instance
g = Graph()

# User input
n = int(input("Enter number of edges: "))
print("Enter edges (node1 node2) one per line:")

for _ in range(n):
    u, v = input().split()
    g.add_edge(u, v)

start_node = input("Enter starting node for DFS: ")

# Perform DFS
print("DFS traversal:")
g.dfs(start_node)

# Visualize the graph
g.visualize()    

"""
5

A B
A C
B D
C E
D E
Enter starting node for DFS: A

"""