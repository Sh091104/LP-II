"""I. Selection Sort (Greedy for Sorting)"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = list(map(int, input("Enter elements to sort (space-separated): ").split()))
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)
"""
29 10 14 37 13
"""


"""II. Single-Source Shortest Path (Greedy: Dijkstra’s Algorithm) """
import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

# Input
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = [[] for _ in range(n)]
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove if directed

start = int(input("Enter starting vertex: "))
distances = dijkstra(graph, start)
print("Shortest distances:", distances)
"""
Enter number of vertices: 5  
Enter number of edges: 6  
Enter edges (u v weight):  
0 1 2  
0 2 4  
1 2 1  
1 3 7  
2 4 3  
3 4 1  
Enter starting vertex: 0

"""


"""IV. Job Scheduling Problem (Greedy for Max Profit with Deadlines)"""
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)
    n = len(jobs)
    max_deadline = max(job[2] for job in jobs)
    slots = [-1] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        id, profit, deadline = job
        for d in range(deadline, 0, -1):
            if slots[d] == -1:
                slots[d] = id
                total_profit += profit
                break

    scheduled = [job for job in slots if job != -1]
    return scheduled, total_profit

n = int(input("Enter number of jobs: "))
jobs = []
print("Enter job as: id profit deadline")
for _ in range(n):
    id, profit, deadline = input().split()
    jobs.append((id, int(profit), int(deadline)))

scheduled, profit = job_scheduling(jobs)
print("Jobs scheduled:", scheduled)
print("Total profit:", profit)
"""
Enter number of jobs: 5  
Enter job as: id profit deadline  
a 100 2  
b 19 1  
c 27 2  
d 25 1  
e 15 3

"""


"""V. Prim’s Minimum Spanning Tree Algorithm"""
import heapq

def prim(graph, start):
    visited = [False] * len(graph)
    pq = [(0, start)]
    mst_cost = 0
    edges = []

    while pq:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        mst_cost += weight
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
                edges.append((u, v, w))
    return mst_cost, edges

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
graph = [[] for _ in range(n)]
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

start = int(input("Enter starting vertex: "))
cost, edges = prim(graph, start)
print("MST Cost:", cost)
print("Edges:", edges)
"""
Enter number of vertices: 3  
Enter number of edges: 3  
Enter edges (u v weight):  
0 1 1  
1 2 2  
0 2 3  
Enter starting vertex: 0

"""


"""VI. Kruskal’s Minimum Spanning Tree Algorithm"""
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            self.parent[pu] = pv
            return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(n)
    mst = []
    cost = 0
    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            cost += w
    return mst, cost

n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
edges = []
print("Enter edges (u v weight):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

mst, cost = kruskal(n, edges)
print("MST edges:", mst)
print("Total cost:", cost)
"""
Enter number of vertices: 4  
Enter number of edges: 5  
Enter edges (u v weight):  
0 1 10  
0 2 6  
0 3 5  
1 3 15  
2 3 4

"""
