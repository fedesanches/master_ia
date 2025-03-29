l1 = [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
l2 = [0, 0, 0, 1, 0, 0]

def propagar(l):
    for i in range(len(l)-1):
        if l[i] == 1 and l[i + 1] == 0: l[i + 1] = 1
    
    """ recorro la lista a la inversa """
    for i in range(len(l)-1, 0, -1):
        if l[i] == 1 and l[i - 1] == 0: l[i - 1] = 1      
    return l

print(l1)
print(propagar(l1))

print(l2)
print(propagar(l2))