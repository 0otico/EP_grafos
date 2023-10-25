#Uma coloração é uma lista c com 2 elementos: c[0] é o grafo em questão e c[1] é a lista das cores de cada vértice.
#c[1][i] é a cor do vértice i+1.
#Cada cor é um número natural.

import grafos as graph

def new(g,w): #cria uma coloração de g, segundo as cores dadas pela lista w
    return [g,w]

def grafo(c): #devolve o grafo associado à coloração c
    return c[0]

def cor(c,v,n): #altera a cor do vértice v para n na coloração c
    d = c[:] #faz uma cópia de c
    d[1][v-1]=n
    return d

def show(c): #devolve os pares (vértice,cor) da coloração c
    for i in range(len(c[1])):
        print ("Vértice", i+1, ":", "cor nº", c[1][i])

def num_erros(c): #devolve o número de erros da coloração c
    erros=0
    i=0
    while i<graph.dim(c[0]):
        j=0
        while j<graph.dim(c[0]):
            if graph.edge(c[0],i+1,j+1): #os pares (i+1,j+1) cobrem todos os pares de vértices de g
                if c[1][i]==c[1][j]: #verifica se as cores de i+1 e de j+1 são iguais
                    erros+=1 #se forem iguais, há um erro
            j+=1
        i+=1
    return erros//2 #cada aresta é verificada 2 vezes

def num_cores(c): #devolve o número de cores distintas usadas em c
 
    def minimo(w): #função que calcula o minimo de uma lista
        res=w[0]
        for x in w:
            if x<res:
                res=x
        return res
    
    check=c[1][:] #copia a lista
    res=0 
    while len(check)!=0: #aproveita o facto de as cores serem representadas por números
        min_aux=minimo(check) 
        res+=1 #conta o número de mínimos (ou cores) que se retira da lista
        i=0
        while i<len(check): #elimina todas as ocorrências do mínimo de check na própria lista check
            if check[i]==min_aux: 
                check=check[:i]+check[i+1:]
                i-=1
            i+=1
    return res

def copyC(c): #cria uma cópia da coloração c
    return new(c[0],c[1][:])
