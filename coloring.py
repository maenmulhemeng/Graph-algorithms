import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue

def coloring(A, s):
   
    colors = {}
    used_colors = {}
    Q = deque() # creates a new Queue object
    
    Q.append(s) # adds the source ‘s’ to the queue
    while len(Q) != 0: # is Q empty?
        u = Q.popleft() # dequeue from queue
        # add u to the current component
        # print('The node',u)
        # print('dd',d)
        # print(Q)
        neighbours_colors= []
        max = -1
        for v in range(len(A[u])): # iterate thru the neighbors of ’u’
            # print('neighbours', A[u][v])
            if A[u][v] == 1:
                if v not in colors: # ‘v’ is unvisited
                    Q.append(v) # add ‘v’ to the queue
                elif v in colors:
                    neighbours_colors.append(colors[v])
                    if max < colors[v]:
                        max = colors[v]
        suitable_color = -1

        for c in range(max):
            exist = False
            for nc in neighbours_colors:
                if c == nc:
                    exist = True
                    break
            if (not exist):
                suitable_color = c
                break
        if suitable_color == -1:
            suitable_color = max +1

        used_colors[suitable_color] =1
        colors[u] =  suitable_color
    return  colors, used_colors

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
 
 V =  {0,1,2,3,4,5,6}
 A =[[0, 1, 0, 0, 1, 0, 0, 0, 0],
     [1, 0, 1, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 1, 1, 0, 0, 0],
     [1, 1, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 1, 0, 0],
     [0, 0, 0, 0 ,0 ,1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 1, 0]]
 
 
 for v in V:
    # while there are nodes to visit
    colors,used_colors = coloring(A,v)
    print ("colors starting from ",v, " is ", colors, ' and number of used colors is ', len(used_colors))        
 # inceremet component #