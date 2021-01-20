
import sys 

def min(d,visited,n):
    min = sys.maxsize
    min_index = 0
    for v in range(n):
        if (d[v] < min) and not visited[v] :
            min = d[v]
            min_index = v

    return min_index
def dijekstra(A, s, d, parent):
    visited = []
    for i in range(len(A)):
        visited.append( False)
        d[i] = sys.maxsize
    
    d[s] =0
        
    for count in range(len(A)):

        u = min(d,visited,len(A))
        visited[u] = True
        
        # print(not_visited)
        for v in range(len(A)):
            if (A[u][v] > 0 and not visited[v]):
                alt = d[u] + A[u][v]
                if (alt < d[v]):
                    d[v] = alt
                    parent[v] = u
       
    return d, parent            

if __name__ == '__main__':
 
 A = [ [ 0, 4, 0, 0, 0, 0, 0, 8, 0 ], 
                        [ 4, 0, 8, 0, 0, 0, 0, 11, 0 ], 
                        [ 0, 8, 0, 7, 0, 4, 0, 0, 2 ], 
                        [ 0, 0, 7, 0, 9, 14, 0, 0, 0 ], 
                        [ 0, 0, 0, 9, 0, 10, 0, 0, 0 ], 
                        [ 0, 0, 4, 14, 10, 0, 2, 0, 0 ], 
                        [ 0, 0, 0, 0, 0, 2, 0, 1, 6 ], 
                        [ 8, 11, 0, 0, 0, 0, 1, 0, 7 ], 
                        [ 0, 0, 2, 0, 0, 0, 6, 7, 0 ] ];

 parent = {}
 d = {} # stores the shortest distance from source ‘s’
 v = 0
 d[v] = 0 # set source dist 0
 parent[v] = 0
 # while there are nodes to visit
 d , parent = dijekstra(A,v,d,parent)
 
 # inceremet component #
print('--------------------')
print ("distances", d)
print ("parents", parent)
