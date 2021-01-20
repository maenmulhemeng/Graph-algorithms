import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue

def transpose(A,n):
    for i in range(n):
        for j in range(i+1,n):
            t = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = t
    return A    
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

    # 0 1 2 3 4 5 6 
   # ------------------
# 0 | 0 1 0 0 1 0 0 
# 1 | 1 0 1 1 1 0 0 
# 2 | 0 1 0 1 0 0 0 
# 3 | 0 1 1 0 1 1 0 
# 4 | 1 1 0 1 0 0 0 
# 5 | 0 0 0 1 0 0 1 
# 6 | 0 0 0 0 0 1 0 

 
 V =  {0,1,2,3,4}
 A =[[0, 1, 0, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 1, 0, 0, 0],
     [0, 0, 1, 0, 0],
     [1, 0, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0 ,0]]
 
 print(A)
 parent = {}
 d = {} # stores the shortest distance from source ‘s’
 d[0] = 0 # set source dist 0
 parent[0] = 0
 # while there are nodes to visit
 component_nodes = BFS_Adj(A,0,d,parent)
 parent = {}
 d = {} # stores the shortest distance from source ‘s’
 
 TA = transpose(A, len(V))
 print(TA)
 d[0] = 0 # set source dist 0
 parent[0] = 0
 component_nodesT = BFS_Adj(TA,0,d,parent)

 print("The results")
 print(component_nodes)
 print(component_nodesT)
 # inceremet component #
 
print('--------------------')
print ("distances", d)
print ("parents", parent)
equaled = True
for i in range(len(component_nodes)):
    exists = False
    for j in range(len(component_nodesT)):
         if (component_nodes[i] == component_nodesT[j]):    
            exists = True
            break
    if not exists:
        equaled = False
        break
if equaled:
    print("Strongly Connected")