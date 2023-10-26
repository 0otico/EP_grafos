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
    Found=False
    Found2= False
    if x!=y:
        while not Found and i<len(g[1]):
            Found= (g[1][i]==(x,y))
            i=i+1
        while ((not Found2)) and f<len(g[1]):
            Found2 = g[1][f]==(y,x)   
            f=f+1
        if Found and Found2:
            return True
        else:
            return False
    else:
        return False

def graphQ(e): # não funciona estou a corrigir
        if type(e)==list:
            if len(e)==2:
                if type(e[0])==int:
                    if type(e[1])==list:
                        j=0
                        intruso=False
                        while j<len(e[1]) and not intruso:
                            intruso= type(e[1][j])!=list
                            print(intruso)
                            j=j+1
                        if not intruso:
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
                                            existe= existe or (e[1][j][0]==e[1][k][1] or e[1][k][0]==e[1][j][1])
                                            k+=1
                                        j+=1

                                        if existe:
                                            l=0
                                            diferente= True
                                            while l<len(e[1]) and diferente:
                                                diferente= (e[1][l][0]!=e[1][l][1])
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
