class Graph:
    def __init__(self, n, m):
        adj = {f"{i + 1}": [] for i in range(n)} # dictionary vertex
        visited = {f"{i + 1}": False for i in range(n)} # dictionary status vertex
        self.is_multygraph = False
        
        
        # input
        for i in range(m):
            a, b = map(str, input().split())
            
            # check multygraph
            if a in adj[b] or b in adj[a]:
                self.is_multygraph = True
                
            adj[a].append(b)
            
            # visited.setdefault(a, False)
            # visited.setdefault(b, False)

        self.n = n # option
        self.m = m # option
        self.adj = adj
        self.visited = visited
        

    def dfs(self, u):
        self.visited[u] = True
        for v in self.adj[u]:
            if not self.visited[v]:
                self.dfs(v)
                
    # def count_component(self):
    #     count = 0
    #     for v in self.visited:
    #         if not self.visited[v]:
    #             self.dfs(v)
    #             count += 1
    #             if count > 1: # option for this problem
    #                 return count
    #     return count
    
def solution():
    # T = int(input())
    # for _ in range(T):
    n, m = map(int, input().split())
    g = Graph(n, m)
    if g.
    for v in g.visited:
        
        if not g.visited[v]:
            g.dfs(v)
            
    if count > 1 or g.is_multygraph:
        print("No")
    else:
        print("Yes")
    
    
    
solution()
        