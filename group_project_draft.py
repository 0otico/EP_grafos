from random import random
from math import pi
from math import log
import cap as cap
import cor  as col
import eventos  as event
import populacao as popu
import individuos as ind

def exprandom(m):
    x=random()
    return -m*log(x)






def sim(Tritmo, Tlimiar, Tfiltro, Tfinal, Tgrafo): #as tres variaveis de tempo, o tempo final, e o grafo a ser utilisado
    ct = 0 #tempo inicial
    gen = 0 #primeiro individuo 0
    T = 100 # populacao atual 
    K = T #populacao inicial
    p = popu.new() #criacao da lista de individuos
    c = cap.new() #criacao da lista de eventos




    w = ["verde"]#lista de cores






    #esta funcao preenche a populacao com T individuos, i poderia estar num modulo, o gen e identificador
    for x in range(T):
        p = popu.addI(p, ind.new(col.new(Tgrafo,w), ct, gen))
        gen += 1

    for x in p: #inicializa os eventos de avaliacao para toda a populacao
        c = cap.add(event.event("avaliacao", ind.ident(x), ct + exprandom(Tlimiar)),c)



    for x in p: #inicializa os eventos de evolucao para toda a populacao
        c = cap.add(event.event("evolucao", ind.ident(x), ct + exprandom(Tritmo)),c)



    #inicializa o evento de filtragem para toda a populacao
    c = cap.add(event.event("selecao", p, ct + exprandom(Tfiltro)),c) 



    
    #ainda falta adicionar one function to be used in case there's an exceduled event for the dead tipo um  
    #if popu.aliveQ(event.ident(e), p):, que devolve True se houver um idividuo na populacao 
    #com o mesmo identificador ao individuo do evento

    
    while Tfinal >= ct:
        e = event.nextE(c)
        if popu.aliveQ(event.ident(e), p):
            if event.kind(e) == "avaliacao": #se o proximo evento for avaliacao
                idx = popu.ident(p, event.ident(e)) #individuo a ser avaliado
                A = ind.coef(idx) #coeficiente de avaliacao do individuo do evento

                I = ct - ind.idade(idx) #idade do idividuo do evento


                if random() <= (1-(2/pi)(1+A)**(1+8(1+I))): # a formula dame um valor de 0 a 1, que sera a probabilidade de ocorrer morte, se o numero aleatorio de 0 a 1 for menor ou igual a esse valor, ele morre.
                    T -= 1
                    p = popu.kill(p,idx) #kills the poor guy

                else:
                    c = cap.add(event.event("avaliacao", idx, ct + exprandom(Tlimiar)), c) #se ele nao morrer, ele ganha outra oportunidade para parar de viver




            elif event.kind(event.next(c)) == "evolucao":
            
                idx1 = popu.ident(p, event.ident(e)) #individuo a ser avaliado

                if random() <= 1/(1+(e**((K-T)/10))): #mutacao
                    idx2 = ind.mutation(idx1) #individuo a ser avaliado mutado
                    if ind.coef(idx2) > ind.coef(idx1): #substitui o antigo pelo novo com cor diferente (mutado), se for melhor
                        popu.kill(idx1) #kill the old
                        popu.addI(idx2) #adds the mutated, replacing him
                    

    
                else:   #reproducao
                    baby = ind.birth(idx1, ct, gen)
                    p = popu.add(p, baby) #adiciona o filho de idx1


                    #updates the population and the gen
                    gen += 1
                    T += 1


                    #creats new events for the new being
                    c = cap.add(event.event("evolucao", baby, ct + exprandom(Tritmo)), c)
                    c = cap.add(event.event("avaliacao", baby, ct + exprandom(Tlimiar)), c)




                c = cap.add(event.event("evolucao", idx1, ct + exprandom(Tritmo)), c) #new events for idx (i don't think i have to specify which because they will have the same gen, not sure tho)



            else: #selecao
                while ind.coef(popu.worst(p)) < 1: #deleta os invalidos
                    popu.kill(popu.worst(p))
                    T -= 1
                while T > K * (3/2): #deleta os validos ate a populacao for de tamanho adequada
                    popu.kill(popu.worst(p))
                    T -= 1

                cap.add(event.event("selecao", p, ct + exprandom(Tfiltro)), c) #novos evento de morte geral




        event.dele(event.nextE(c)) #acabou o evento atual, passamos para o proximo 
        ct = event.date(event.nextE(c)) #data do proximo evento