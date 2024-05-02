class Graph:
    def __init__(self):
        self.graph={}
    
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def dfs(self,start,visited=None):
        if visited is None:
            visited=set()
        visited.add(start)
        print(start,end=' ')

        for neighbor in self.graph[start]:
             if neighbor not in visited:
                self.dfs(neighbor,visited)

g=Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth First Traversal starting from vertex 2:")
g.dfs(2)
