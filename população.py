#Uma população eé uma lista p de indivíduos

import grafos as graph
import colorações as color
import indivíduos as ind
import random as random

#new() - cria uma população nova
def new():
    return []

#dim(p) - devolve o número de elementos da população
def dim(p):
    return len(p)


#identQ(p,i) - verifica se algum indivíduo de p tem o identificador i
def identQ(p,i):
    k=0
    found=False
    while k<len(p) and not found:
        found = ind.ident(p[k])==i
        k+=1
    return found

    
#ident(p,i) - devolve o indivíduo da população p com o identificador i
def ident(p,i):
    if identQ(p,i): #só vai procurar se o indivíduo exisitr
        k=0
        found=False
        while k<len(p) and not found:
            if ind.ident(p[k])==i:
                found=True
            else:
                k+=1
        return p[k]
    

#best(p) - devolve o indivíduo de p com melhor coeficiente de adaptação
def best(p):
    best=ind.coef(p[0]) 
    res=p[0]
    for x in p[1:]:
        if ind.coef(x)>best:
            best=ind.coef(x)
            res=x
    return res

#worst(p) - devolve o indivíduo de p com pior coeficiente de adaptação 
def worst(p):
    worst=ind.coef(p[0])
    res=p[0]
    for x in p[1:]:
        if ind.coef(x)<worst:
            worst=ind.coef(x)
            res=x
    return res

#addI(p,i) - adiciona o indivíduo i à população p e devolve p
def addI(p,i):
    p+=[i]
    return p

#kill(p,i) - tira o indivíduo com identificador i da lista p
def kill(p,i):
    res=[]
    n = 0
    while n < dim(p):
        if ind.ident(p[n])!=ind.ident(i):
            res+=[p[n]]
        n += 1
    return res
