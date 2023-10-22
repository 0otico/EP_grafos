#Um grafo é uma lista de listas g, em que g[i] corresponde ao vértice i+1; os elementos de g[i] são os vértices ligados a i+1.
# - Cada vértice é um número natural
# - O número de vértices corresponde a len(g)
# - Cada aresta (x,y) aparece representada 2 vezes: y aparece na lista de x, e x aparece na lista de y

def new(n): #cria um grafo com n vértices, e sem arestas
    return [[] for x in range(n)]

def addedge(g,x,y): #adiciona a aresta (x,y) ao grafo g
    if not y in g[x-1] and x!=y: 
        #só adiciona a aresta se ela não existir
        #um dos vértices não pode ter arestas para si mesmo, senão nenhuma coloração é válida
        #em princípio, se y pertence a g[x-1] então x pertence a g[y-1]
        g[x-1]=[n for n in g[x-1] if n<y]+[y]+[n for n in g[x-1] if n>y]
        g[y-1]=[n for n in g[y-1] if n<x]+[x]+[n for n in g[y-1] if n>x]
    return g

def deledge(g,x,y): #remove a aresta (x,y) do grafo g
    if y in g[x-1] and x!=y: #mesma lógica que addedge
        g[x-1]=[n for n in g[x-1] if n<y]+[n for n in g[x-1] if n>y]
        g[y-1]=[n for n in g[y-1] if n<x]+[n for n in g[y-1] if n>x]
    return g

def dim(g): #devolve o número de vértices de g
    return len(g)

def emptyQ(g): #verifica se o gráfico é vazio (não tem arestas)
    res=True
    i=0
    while i<len(g) and res: #para quando encontrar um False ou quando tiver visto as listas todas
        res= (len(g[i])==0) #verifica se todas as listas de g são vazias
        i+=1
    return res

def edge(g,x,y): #verifica se a aresta (x,y) existe em g
    if y in g[x-1] and x in g[y-1] and x!=y:
        return True
    else:
        return False
    
def graphQ(g): #verifica se g é um grafo
    
    if type(g)==list: #g tem de ser uma lista
        res=True
        i=0
        while i<len(g) and res: 
            res=(type(g[i])==list)
            i+=1
            
        if res: #os elementos de g têm de ser listas
            i=0
            while i<len(g) and res:
                res=(len(g[i])<=len(g))
                i+=1
                
            if res: #as listas de g não podem ter mais elementos do que o número de vértices de g
                i=0
                while i<len(g) and res:
                    j=0
                    while j<len(g[i]) and res:
                        res=(type(g[i][j])==int)
                        j+=1
                    i+=1
                    
                if res: #os elementos das listas de w têm de ser inteiros
                    i=0
                    while i<len(g) and res:
                        j=0
                        while j<len(g[i]) and res:
                            res=(g[i][j]>0 and g[i][j]<=len(g) and g[i][j]!=i+1)
                            #o g[i][j]!=i+1 serve para garantir que os vértices não ligam a si mesmos
                            j+=1
                        i+=1
                            
                    if res: #os elementos das listas de g têm de estar entre 1 e len(g) (para representar vértices)
                        i=0
                        while i<len(g) and res:
                            j=0
                            while j<len(g[i]) and res:
                                n=g[i][j]
                                res=(i+1 in g[n-1])
                                j+=1
                            i+=1
                        
                        return res #se n está na lista do vértice i+1 (g[i]), então i+1 tem de estar na lista de n (g[n-1])
                        
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
