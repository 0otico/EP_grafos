def newgraph(N):
    return [N,[]]



def addedge(g,x,y):
    i=0
    Found= False
    if x!=y:
        while not Found and i<len(g[1]):
            Found= (g[1][i]==(x,y))
            i=i+1
        if Found:
            return g
        else:
            return [g[0],g[1]+[(x,y)]+[(y,x)]]
    else:
        return g
            
def deledge(g,x,y):
    if x!=y:
        i=0
        f=0
        Found=False
        Found2=False
        while ((not Found)) and i<len(g[1]):
            Found= (g[1][i]==(x,y))
            i+=1
        while ((not Found2)) and f<len(g[1]):
            Found2 = g[1][f]==(y,x)   
            f=f+1
        if not((Found) and (Found2)):
            return g
        else:
            if i<f:
                g=[g[0],g[1][:i-1]+g[1][i:f-1]+g[1][f:]]
                return g
            else:
                g=[g[0],g[1][:f-1]+g[1][f:i-1]+g[1][i:]]
                return g
    else:
        return g

        



def dim(g):
    return g[0]
def emptyQ(e):
    return len(e[1])==0


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

def graphQ(e):
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
                            while j<len(e[1]):
                                k=0
                                existe= True 
                                while k<len(e[1]) and existe:
                                    existe= e[1][j]==e[1][k]
                                    k+=1
                                if existe:
                                    l=0
                                    while l<len(e[1]):
                                        l=0
                                        diferente= diferente and (e[1][l][0]==e[1][l][1])
                                        l+=1
                                    return diferente
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
