# Uma agenda (CAP) é uma lista c de eventos.

import eventos as event

def new(): #cria uma agenda vazia
    return []

def add(e,c): #adiciona o evento e à agenda c
    #mantém a agenda ordenada por instante dos eventos
    return [n for n in c if event.time(n)<=event.time(e)]+[e]+[n for n in c if event.time(n)>event.time(e)] 

def nextE(c): #devolve o próximo evento na agenda c
    return c[0]

def delete(c): #elimina o primeiro evento da agenda c
    return c[1:]
