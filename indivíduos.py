
import grafos as graph
import colorações as color
import random as random
import copy
#Indivíduos  - Lista i com 3 elementos: i[0] é a coloração correspondente, i[1] é o momento em que nasceram, i[2] é o identificador

#new(c,t,n) - cria um indivíduo com a coloração c, nascido no momento t, com o identificador n (devolve o indivíduo criado)
def new(c,t,n):
    return[c,t,n]

#coef(i) - devolve o coeficiente de adaptação de i
def coef(i):
    if color.num_erros(i[0])==0:
        return graph.dim(color.grafo(i[0]))/color.num_cores(i[0])
    else:
        return 1/(color.num_erros(i[0])+1)


#idade(i) - devolve o momento de criação de i
def idade(i):
    return i[1]


#mutation(i) - altera uma cor na coloração de i (devolve o indivíduo evoluído)
def mutation(i):
    v=random.randrange(1,graph.dim(color.grafo(i[0]))+1)
    n=random.randrange(1,color.num_cores(i[0])+1)
    i[0]=color.cor(i[0],v,n)
    return i


#ident(i) - devolve o identificador do indivíduo 
def ident(i):
    return i[2]


#color(i) - devolve a coloração do indivíduo
def colour(i):
    return i[0]

def copyI(i):
    return new(color.copyC(i[0]),i[1],i[2])

