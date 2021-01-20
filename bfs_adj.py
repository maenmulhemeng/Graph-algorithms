import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue

def BFS_Adj(A, s, d, parent):
    compoenent_nodes = [s]
    Q = deque() # creates a new Queue object
    
    Q.append(s) # adds the source ‘s’ to the queue
    while len(Q) != 0: # is Q empty?
        u = Q.popleft() # dequeue from queue
        # add u to the current component
        # print('The node',u)
        # print('dd',d)
        # print(Q)
        for v in range(len(A[u])): # iterate thru the neighbors of ’u’
            # print('neighbours', A[u][v])
            if A[u][v] == 1 and v not in d: # ‘v’ is unvisited
                d[v] = d[u] + 1 # update shortest path distance of ‘v’
                parent[v] = u
                compoenent_nodes.append(v)
                Q.append(v) # add ‘v’ to the queue
    return compoenent_nodes

if __name__ == '__main__':

    # 0 1 2 3 4 5 6 7 8 
   # ------------------
# 0 | 0 1 0 0 1 0 0 0 0
# 1 | 1 0 1 1 1 0 0 0 0
# 2 | 0 1 0 1 0 0 0 0 0
# 3 | 0 1 1 0 1 1 0 0 0
# 4 | 1 1 0 1 0 0 0 0 0
# 5 | 0 0 0 1 0 0 1 0 0
# 6 | 0 0 0 0 0 1 0 0 0
# 7 | 0 0 0 0 0 0 0 0 1
# 8 | 0 0 0 0 0 0 0 1 0
 
 V =  {0,1,2,3,4,5,6,7,8}
 A =[[0, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0 ,0 ,1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0]]
 
 parent = {}
 d = {} # stores the shortest distance from source ‘s’

 component_no = 0
 for v in V:
     if v not in d :
        component_no = component_no + 1 
        print("-------  component ",component_no)
        d[v] = 0 # set source dist 0
        parent[v] = 0
        # while there are nodes to visit
        component_nodes = BFS_Adj(A,v,d,parent)
        print(component_nodes)
 # inceremet component #
print('--------------------')
print ("distances", d)
print ("parents", parent)
