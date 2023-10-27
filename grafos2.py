# Grafo corresponde a uma lista em que a posição 0 diz-nos quantos vértices o grafo tem
# e a posição 1 é uma lista que possui todas os pares de arestas (tuplos)
#Tem-se que cada par de arestas (x,y) aparece também (y,x); os vértices são números inteiros; 
#não podem existir arestas para o próprio vértice, pois assim nenhuma coloração seria válida

def new(N): #grafo com n vértices e nehuma aresta
    return [N,[]] #devolve o grafo criado


def addedge(g,x,y): #acrescenta arestas ao grafo
    i=0
    Found= False
    if x!=y: #não pode acrescentar uma aresta para o próprio vértice
        while not Found and i<len(g[1]): #verificar que não existe já no grafo
            Found= (g[1][i]==(x,y)) 
            i=i+1
        if Found:
            return g #se existir retorna o grafo
        else:
            return [g[0],g[1]+[(x,y)]+[(y,x)]] # se não, acrescenta
    else:
        return g


def deledge(g,x,y): #apaga arestas do grafo
    if x!=y: #não pode acrescentar uma aresta para o próprio vértice
        i=0
        f=0
        Found=False
        Found2=False
        while ((not Found)) and i<len(g[1]):  #verificar que existe no grafo
            Found= (g[1][i]==(x,y)) 
            i+=1
        while ((not Found2)) and f<len(g[1]): #verificar que existe no grafo a aresta correspondente para o sentido oposto
            Found2 = g[1][f]==(y,x)   
            f=f+1
        if not((Found) and (Found2)): #se não estiverem no grafo retornar o grafo
            return g 
        else:   #se estiverem no grafo temos dois casos
            if i<f:
                g=[g[0],g[1][:i-1]+g[1][i:f-1]+g[1][f:]] #apagar as arestas
                return g
            else:
                g=[g[0],g[1][:f-1]+g[1][f:i-1]+g[1][i:]] #apagar as arestas
                return g
    else:
        return g


def dim(g):      #dá o número de vértices do grafo
    return g[0]


def emptyQ(e):   #vê se o grafo é vazio 
    return len(e[1])==0 #retorna verdadeiro ou falso consoante a avaliação


def edge(g, x, y):  #vê se a aresta se encontra no grafo
    if x != y:  #vê se não há aresta para o próprio vértice
        existearesta=False
        for edge in g[1]:
            if (x, y) == edge or (y, x) == edge: #a aresta está no grafo
                existearesta = True
        return existearesta
    else:
        return False

def graphQ(e): #verifica se é um grafo
    if type(e)==list: #verifica se é uma lista
        if len(e)==2: #essa lista tem duas posições
            if type(e[0])==int: #a primeira posição corresponde a um inteiro
                if type(e[1])==list: #a segunda é uma lista
                    if e[1]==[]:      # se essa lista For vazia é um grafo
                        return True
                    j=0
                    intruso=False    
                    while j<len(e[1]) and not intruso: #verificar que é uma lista de tuplos
                        intruso= type(e[1][j])!=tuple
                        j=j+1
                    if not intruso:
                        i=0
                        notfound=True
                        while notfound and i<len(e[1]): #verifica se todos os tuplos têm duas posições (são arestas)
                            notfound= len(e[1][i])==2
                            i+=1
                        if notfound:
                            if len(list_nodes(e))<=e[0]: #confirma se a arestas não estão entre vértices que não existem no grafo
                                j=0
                                while j<len(e[1]):  #verifica se cada par de arestas (x,y) tem um oposto (y,x) que lhe corresponde
                                    k=0
                                    existe= True 
                                    while k<len(e[1]) and existe:
                                        existe= existe or (e[1][j][0]==e[1][k][1] or e[1][k][0]==e[1][j][1])
                                        k+=1
                                    j+=1
                                    if existe:
                                        l=0
                                        diferente= True
                                        while l<len(e[1]) and diferente:  #verifica que não há arestas para o próprio vértice
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
            
        
def list_nodes(g):  #função auxiliar que numa lista coloca todos os vértices que têm ligação com outros vértices
    l=[]
    for e in g[1]:
        if not e[0] in l:
            l+= [e[0]]
        if not e[1] in l:
            l+= [e[1]]
    return l
