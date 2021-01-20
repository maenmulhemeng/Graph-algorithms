import numpy as np
def Bellman_Ford(A,s):
 n = len(A)
 d = np.full(n,99) # initialize distance vector
 p = {} # holds parents
 p[0] = s
 d[s] = 0
 d_old = d.copy()
 for k in range(0,n): # do n-1 steps
  print ("vector d:", d)
  for j in range(0,n):
    sum_d = d_old + A[:,j].T # add for node j
    min_val = min(sum_d)
    if min_val < d[j]: # update d
        d[j] = min_val
        p[j] = np.argmin(sum_d)
        d_old = d.copy()
  return d, p
if __name__ == "__main__":
    B = np.array([[99,8,99,99,1],[8,99,7,3,2], [99,7,99,1,99],[99,3,1,99,6],[1,2,99,6,99]])
    print(B[:,0])
    r = Bellman_Ford(B,0)
    print(r)