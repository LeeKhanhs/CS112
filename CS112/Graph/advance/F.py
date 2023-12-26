class Graph:
    def __init__(self, n):
        self.adj = {str(i): [] for i in range(n)}
        self.visited = {str(i): 0 for i in range(n)}
        self.low = {str(i): None for i in range(n)}
        self.bridge = 0
        self.count = 0
                
        # input
        while True:
            a, b = map(str, input().split())
            if a == "-1":
                break
                        
            self.adj[a].append(b)
            self.adj[b].append(a)
            
    # Thuáº­t toÃ¡n tajan        
    def dfs(self, u, par):
        self.count += 1 # indexing
        self.low[u] = self.visited[u] = self.count # for first time, the low[u] is itself

        for v in self.adj[u]:
            if v != par: # Skip the parent node to avoid going back
                if self.visited[v] == 0:
                    self.dfs(v, u)
                    self.low[u] = min(self.low[u], self.low[v]) # update the lowest vertex u can go
                    if self.low[v] == self.visited[v]: # Check if the lowest vertex v can reach is greater than or equal to its own index
                        self.bridge += 1
                else: # has a path from v -> u again
                    self.low[u] = min(self.low[u], self.visited[v]) # update the lowest vertex u can go
                    
    
    def count_bridge(self):
        for u in self.visited:
            if self.visited[u] == 0:
                self.dfs(u, u)
                
    
    

def solution():
    n = int(input())
    g = Graph(n)
    g.count_bridge()
    print(g.bridge)

if __name__ == "__main__":
    solution()