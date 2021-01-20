import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue


def hasCycle(G, s):
 parent = {}
 visited = {}
 Q = deque() # creates a new Queue object
 parent[s] = s
 Q.append(s) # adds the source ‘s’ to the queue
 while len(Q) != 0: # is Q empty?
    u = Q.popleft() # dequeue from queue
    visited[u] = True
    # add u to the current component
    for v in G.neighbors(u): # iterate thru the neighbors of ’u’
        if v not in visited: # ‘v’ is unvisited
            parent[v] = u
            Q.append(v) # add ‘v’ to the queue
        elif parent[u] != v:
            return True
 return False


if __name__ == '__main__':
 G = nx.Graph()
 # L = [(0,1),(1,2),(2,3),(1,3),(3,4),(1,4),(0,4),(3,5),(5,6),(7,8)]
 L = [(0,1),(1,2),(1,3),(3,4),(2,4)]
 G.add_edges_from(L)
 nx.draw(G, with_labels=True)
 
 plt.savefig('graph.png')
 
 
 # while there are nodes to visit
 result = hasCycle(G,0)
 # inceremet component #
 print('--------------------')
 print ("Has cycle", result)
