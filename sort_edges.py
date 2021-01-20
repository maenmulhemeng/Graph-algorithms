def sort_edges_asceding(E):
    e = len(E)
    for i in range(e):
        #print("process ", p, " : ", E[i][1])
        for j in range(i+1,e):
            
            if (E[i][2] > E[j][2]):
                temp = E[i]
                E[i] = E[j]
                E[j] = temp
    
    return E

def sort_edges(E):
    e = len(E)
    for i in range(e):
        #print("process ", p, " : ", E[i][1])
        for j in range(i+1,e):
            
            if (E[i][2] < E[j][2]):
                temp = E[i]
                E[i] = E[j]
                E[j] = temp
    
    return E