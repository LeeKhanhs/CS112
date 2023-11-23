class Edge:
    def __init__(self, a, b, w):
        self.x = (a,b)
        self.w = w

class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        edges = []
        vertices = set()
        while True:
            a, b, w = map(str, input().split())
            if a == "-1":
                break
            w = int(w)
            # if a not in vertices:
            #     vertices.append(a)
            # if b not in vertices:
            #     vertices.append(b)
            vertices.update([a,b])    
            edge = Edge(a, b, w)
            edges.append(edge)
        
        self.vertices = vertices
        self.edges = edges
    
    def find_weight_MSP(self):
        
        edges = sorted(self.edges, key=lambda x: x.w)
        n_edges = len(edges)
        parrent = {str(i): str(i) for i in range(self.n_vertices)}
        total_w = 0
        vertices = self.vertices
        MST = []
        pivot = 0
        while len(MST) != self.n_vertices - 1 and pivot < n_edges:
            edge = edges[pivot]
            a, b = edge.x
            root_a = parrent[a]
            root_b = parrent[b]
            if root_a != root_b:
                for vertice in vertices:
                    if parrent[vertice] == root_b:
                        parrent[vertice] = root_a
                total_w += edge.w
                MST.append(edge)
            pivot += 1
        return total_w
    
def solution():
    n_vertices = int(input())
    g = Graph(n_vertices)
    print(g.find_weight_MSP())
    
if __name__ == "__main__":
    solution()
    

        