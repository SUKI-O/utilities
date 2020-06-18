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

    def DFS_loop(self,v, visited):
        visited[v] = True
        print(v, end='')
        scc.append(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_loop(i, visited)

    def DFS(self, v, stack):
        visited= [False]*(self.V)
        self.DFS_loop(v, visited)

    def fillOrder(self,v,visited, stack): 
            # Mark the current node as visited 
            visited[v]= True
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[v]: 
                if visited[i]==False: 
                    self.fillOrder(i, visited, stack) 
            stack = stack.append(v) 
    
    def printSCC(self):
        scc_list = []
        visited = [False]*self.V
        stack= []
        for i in range(self.V):
            if visited[i]==False:
                self.fillOrder(i,visited, stack)
        #print('stack:', stack)
        g_rev = g.reverse_graph()
        visited = [False]*self.V
        scc = []
        while stack:
            i = stack.pop()
            if visited[i]==False:
                g_rev.fillOrder(i, visited, scc)
                #print('')
                scc_list.append(scc)
                scc= []
        return scc_list

N = 875715
# g = Graph(7)
# g.addEdge(0,1)
# g.addEdge(1,2)
# g.addEdge(1,4)
# g.addEdge(2,0)
# g.addEdge(2,3)
# g.addEdge(2,6)
# g.addEdge(3,0)
# g.addEdge(4,2)
# g.addEdge(4,5)

import os
os.chdir('C:\\Users\\ituki\\Documents\\Classes\\Coursera\\Coursera_Algo')
source=[]
f = lambda x,y : [int(x),int(y)]
for line in open('SCC.txt'):
    source.append(f(line.split()[0], line.split()[1]))

N = 875714+1
g = Graph(N)
for  i in range(1,len(source)):
    u,v = source[i]
    g.addEdge(u,v)
import sys
sys.setrecursionlimit(N)
scc_list = g.printSCC()
#[print(scc) for scc in scc_list]
print(scc_list)