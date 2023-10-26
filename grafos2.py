def newgraph(N):
    return [N,[]]

def edge_index(g,x,y):
    i=0
    f=0
    notFound=True
    notFound2=True
    while (notFound or notFound2) and i<len(g[1]):
        notFound= g[1][i]==(x,y)
        notFound2= g[1][f]==(y,x)
        f=f-1
        i=i-1
    return i

def addegde(g,x,y):
    i=0
    notFound=True
    if x!=y:
        while notFound and i<len(g[1]):
            notFound= (g[1][i]==(x,y) and g[1][i]==(y,x))
            i=i+1
        if notFound:
            return g
        else:
            return [g[0],g[1]+[(x,y)]+[(y,x)]]
    else:
        return g
            
def delegde(g,x,y):
    i=0
    f=0
    notFound=True
    if x!=y:
        while notFound and i<len(g[1]):
            notFound= (g[1][i]==(x,y) and g[1][f]==(y,x))
            i=i+1
            f=f+1
        if notFound:
            return g
        else:
            if i<f:
                return [g[0],g[1][:i-1]+g[1][i:f-1][f:]]
            else:
                return [g[0],g[1][:f-1]+g[1][f:i-1]+g[1][i:]]
    else:
        return g

        

def addegde(g,x,y):
    i=edge_index(g,x,y)
    if i==len(g[1]):
        return [g[0],g[1]+[(x,y)]+[(y,x)]]
    else:
        return g

def deledge(g,x,y):
    i=edge_index(g,x,y)
    return [g[0],g[1][:i-1]+g[1][i:]]

def dim(g):
    return g[0]
def emptyQ(e):
    return len(e[1])==0

def edge(g,x,y):
    return not len(g[1])==edge_index(g,x,y)

def edge(g,x,y):
    i=0
    f=0
    notFound=True
    if x!=y:
        while notFound and i<len(g[1]):
            notFound= (g[1][i]==(x,y) and g[1][f]==(y,x))
            i=i+1
            f=f+1
        if notFound:
            return False
        else:
            return True
    else:
        return False

def graphQ(e): #não funciona estou a corrigir
    if type(e)==list:
        if len(e)==2:
            if type(e[0])==int:
                if type(e[1])==list:
                    i=0
                    notfound=True
                    while notfound and i<len(e[1]):
                        notfound= len(e[1][i])==2
                        i+=1
                    if notfound:
                        if len(list_nodes(e))<=e[0]:
                            j=0
                            while j<len(g[1]):
                                k=0
                                existe= True 
                                while k<len(g[1]) and existe:
                                    existe= g[1][j]==g[1][k]
                                if existe:
                                    l=0
                                    while l<len(g[1]):
                                        k=0
                                        diferente= diferente and (g[1][k][0]==g[1][k][0])
                                    return diferente
                                else:
                                    return false    
                            else:
                                return False
                    else: 
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
        
def list_nodes(g):
    l=[]
    for e in g[1]:
        if not e[0] in l:
            l+= [e[0]]
        if not e[1] in l:
            l+= [e[1]]
    return l

