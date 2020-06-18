from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list)

    def addEdge(self, u,v):
        self.graph[u].append(v)
    
    def reverse_graph(self):
        reversed = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                reversed.addEdge(j,i)
        return reversed

    def BFS(self, s):
        visited = [False]*(self.V)
        queue = []
        queue.append(s)
        visited[s]= True

        while queue:
            s = queue.pop(0)
            print(str(s), end='')

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i]= True
                    queue.append(i)

    def DFS_loop(self,v, visited, stack):
        visited[v] = True
        print(v, end='')
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_loop(i, visited, stack)

    def DFS(self, v, stack):
        visited= [False]*(max(self.graph)+1)
        self.DFS_loop(v, visited, stack)

    # def fillOrder(self,v,visited, stack): 
    #         # Mark the current node as visited 
    #         visited[v]= True
    #         #Recur for all the vertices adjacent to this vertex 
    #         for i in self.graph[v]: 
    #             if visited[i]==False: 
    #                 self.fillOrder(i, visited, stack) 
    #         stack = stack.append(v) 
    
    def printSCC(self):
        visited = [False]*self.V
        stack= []
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i,visited, stack)
        print('stack:', stack)
        g_rev = g.reverse_graph()
        while stack:
            i = stack.pop()
            g_rev.DFS





g = Graph(7)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,1)
g.addEdge(1,4)
g.addEdge(4,5)
g.addEdge(5,6)
g.addEdge(6,4)

g.printSCC()