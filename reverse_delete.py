import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue
from sort_edges import sort_edges
from disconected import is_disconected

  

if __name__ == '__main__':
    G = nx.Graph()
    
    E = [(0,1,8),(0,5,2),(1,2,5),(1,4,4),(1,5,1),(2,3,9),(2,4,7),(3,4,6),(4,5,3)]
    G.add_weighted_edges_from(E)
    L = sort_edges(E)
    print(L)
    mst = []
    nodes = {}
    for e in L:
        mst.append(e)
        G.remove_edge(e[0],e[1])
        if (is_disconected(G)):
            #print(e)
            G.add_weighted_edges_from([e])
            mst.remove(e)
           
        

    nx.draw(G, with_labels=True)
    plt.savefig('graph.png')

    

    # inceremet component #
print('--------------------')
print ("MST ", mst)
