import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue


def BFS(G, s, d, parent):
 compoenent_nodes = [s]
 Q = deque() # creates a new Queue object
 
 Q.append(s) # adds the source ‘s’ to the queue
 while len(Q) != 0: # is Q empty?
    u = Q.popleft() # dequeue from queue
    # add u to the current component
    for v in G.neighbors(u): # iterate thru the neighbors of ’u’
        if v not in d: # ‘v’ is unvisited
            d[v] = d[u] + 1 # update shortest path distance of ‘v’
            parent[v] = u
            compoenent_nodes.append(v)
            Q.append(v) # add ‘v’ to the queue
 return compoenent_nodes


if __name__ == '__main__':
 G = nx.Graph()
 L = [(0,1),(1,2),(2,3),(1,3),(3,4),(1,4),(0,4),(3,5),(5,6),(7,8)]
 G.add_edges_from(L)
 nx.draw(G, with_labels=True)
 parent = {}
 d = {} # stores the shortest distance from source ‘s’
 plt.savefig('graph.png')
 component_no = 0
 for v in G.nodes:
     if v not in d :
        component_no = component_no + 1 
        print("-------  component ",component_no)
        d[v] = 0 # set source dist 0
        parent[v] = 0
        # while there are nodes to visit
        component_nodes = BFS(G,v,d,parent)
        print(component_nodes)
 # inceremet component #
print('--------------------')
print ("distances", d)
print ("parents", parent)
