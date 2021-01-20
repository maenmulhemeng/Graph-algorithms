import networkx as nx # graph
import pylab as plt # plotting
from collections import deque # queue
from cycle import hasCycle
from sort_edges import sort_edges_asceding



if __name__ == '__main__':
    G = nx.Graph()
    
    E = [(0,1,8),(0,5,1),(1,2,4),(1,4,3),(1,5,2),(2,3,6),(2,4,8),(3,4,5),(4,5,7)]
    G.add_weighted_edges_from(E)
    L = sort_edges_asceding(E)
    print(L)
    mst = []
    for e in L:
        mst.append(e)
        t = nx.Graph()
        t.add_weighted_edges_from(mst)
        if (hasCycle(t,e[0])):
            mst.remove(e)

    nx.draw(G, with_labels=True)
    plt.savefig('graph.png')

    

    # inceremet component #
print('--------------------')
print ("MST ", mst)
