
import sys 

def min(borders):
    min = sys.maxsize
    min_index = 0
    for v in borders:
        if (borders[v] < min) :
            min = borders[v]
            min_index = v
    return min_index

def removeFromBoarders(borders,x):
    toRemove = []
    for v in borders:
        for k in v:
            if k == x:
                toRemove.append(v)
    for v in toRemove:
        borders.pop(v)
    
def prims(A, s, parent):
    borders = {}
    visited = []
    parent[s] = s
    for v in range(len(A)):
        visited.append(False)
        if (A[s][v] > 0):
            borders[(s,v)] = A[s][v] 
    u = s   
    
   
    while len(borders) > 0:
        # print(borders)
        # print(visited)
        x = min(borders)
        visited[u] = True
        v =  0
        for t in x:
            if t != u:
                v = t
        parent[v] = u
        print(v)
        removeFromBoarders(borders,v)

        for k in range(len(A)):
            if (A[v][k] > 0) and not visited[k]:
                 borders[(v,k)] = A[v][k]
        u = v        
    return  parent            

if __name__ == '__main__':
 
 A = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
       [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
       [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
       [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
       [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
       [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
       [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
       [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
       [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ]

 A = []
 n = 6
 for i in range(n):
     A.append([])
     for j in range(n):
         A[i].append(0)
 A[0][1] = 8
 A[0][5] = 1
 A[1][0] = 8
 A[1][5] = 2
 A[1][4] = 3
 A[1][2] = 4
 A[2][4] = 9
 A[2][3] = 5
 A[2][1] = 4
 A[3][2] = 5
 A[3][4] = 7
 A[4][1] = 3
 A[4][2] = 9
 A[4][5] = 6
 A[4][3] = 7
 A[5][0] = 1
 A[5][1] = 2
 A[5][4] = 4 
   
 parent = {}
 v = 0
 parent[v] = 0
 # while there are nodes to visit
 parent = prims(A,v,parent)
 
 # inceremet component #
print('--------------------')

print ("parents", parent)
