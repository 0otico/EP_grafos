# Uma agenda (CAP) é uma lista c de eventos.
# O nome da agenda pode mudar com as várias operações (add, delete, delete_id)

import eventos as event

def new(): #cria uma agenda vazia
    return []

def add(e,c): #adiciona o evento e à agenda c
    #parte do pressuposto que c está ordenada
    return [n for n in c if event.time(n)<=event.time(e)]+[e]+[n for n in c if event.time(n)>event.time(e)] 

def nextE(c): #devolve o próximo evento na agenda c
    return c[0]

def delete(c): #elimina o primeiro evento da agenda c
    return c[1:]

def delete_id(c,i): #elimina os eventos respeitantes ao indivíduo i da agenda c
    res=[]
    for x in c:
        if not event.ident(x)==i: 
            res+=[x] #adiciona ao resultado os eventos que não dizem respeito ao indivíduo i
    return res