mylist = [2,35, 5,6,1,0,4,10,34]
n = len(mylist)
print(mylist)


def merge(a,b):
    aCounter = 0
    bCounter = 0
    # print('---------------------')
    # print(a)
    # print(b)
    aList = []
    while (aCounter < len(a) and bCounter < len(b)):
        # print ('here')
        if (a[aCounter] < b[bCounter]):
            aList.append(a[aCounter])
            aCounter = aCounter + 1
        else:
            aList.append(b[bCounter])
            bCounter = bCounter + 1
    
    if (aCounter >= len(a)):
       while (bCounter < len(b)):
            aList.append(b[bCounter])
            bCounter = bCounter + 1
    if (bCounter >=len(b)):
       while (aCounter < len(a)):
            aList.append(a[aCounter])
            aCounter = aCounter + 1
    # print(aList)
    return aList
    
def divide(aList):
    n = len(aList)
    # print(n)
    if (n == 0):
        return []
    elif (n == 1):
        return aList
    else:
        l1 = aList[0:int(n/2)]
        # print(l1)
        l2 = aList[int(n/2):n]
        # print(l2)
        a = divide(l1)
        b = divide(l2)
        
        aList = merge(a,b)
      
    return aList
print (divide(mylist))

mylist[2], mylist[1] = mylist[1], mylist[2]

print (mylist)        