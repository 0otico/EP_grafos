#módulos
import grafos as graph 
import colorações as color 
import indivíduos as ind 
import população as pop 
import eventos as event 
import CAP as cap
import copy

#para fazer contas de probabilidade
import random as random #extensão com random, randrange
from math import pi 
from math import log 
from math import e
from math import atan
from math import ceil

def exprandom(m):
    x=random.random()
    return -m*log(x)


def simulador(G, K, Tfim, Tritmo, Tlimiar, Tfiltro): 
#G é o grafo; K é a dimensão da população inicial; Tfim é a duração da simulação; 
#Tritmo, Tlimiar e Tfiltro são as variáveis dos eventos

    #verificar que as variáveis são válidas
    if not graph.graphQ(G):
        return 'Erro: a variável G tem de ser um grafo'
    if type(K)!=int or K<=0:
        return 'Erro: a variável K tem de ser um número inteiro positivo'
    if (type(Tfim)!=float and type(Tfim)!=int) or Tfim<=0:
        return 'Erro: a variável Tfim tem se ser um número positivo'
    if (type(Tritmo)!=float and type(Tritmo)!=int) or Tritmo<=0:
        return 'Erro: a variável Tritmo tem de ser um número positivo'
    if (type(Tlimiar)!=float and type(Tlimiar)!=int) or Tlimiar<=0:
        return 'Erro: a variável Tlimiar tem de ser um número positivo'
    if (type(Tfiltro)!=float and type(Tfiltro)!=int) or Tfiltro<=0:
        return 'Erro: a variável Tfiltro tem de ser um número positivo'

    #inicalizar as variáveis
    CurrentTime = 0 #o instante em que estamos
    identificador = 1 #identificador do próximo indivíduo a ser criado
    população = pop.new() #cria a lista de individuos
    CAP = cap.new() #cria a lista de eventos

    #inicializar a população e a CAP
    for k in range(K):
        cores = [x+1 for x in range(graph.dim(G))]
        coloracao = color.new(G, cores)
        indivíduo = ind.new(coloracao, CurrentTime, identificador) #cria o indivíduo novo 
        população = pop.addI(população, indivíduo) #junta o indivíduo novo à população
        avaliação = event.event("avaliação", identificador, CurrentTime + exprandom(Tlimiar)) #próxima avaliação do novo indivíduo
        CAP = cap.add(avaliação, CAP) #adiciona a avaliação à CAP
        evolução = event.event("evolução", identificador, CurrentTime + exprandom(Tritmo)) #próxima evolução do novo indivíduo
        CAP = cap.add(evolução, CAP) #adiciona a evolução à CAP
        identificador += 1
        
    #próximo evento de seleção global
    seleção = event.event("seleção", 0, CurrentTime+exprandom(Tfiltro)) #0 serve como default, porque a seleção afeta todos
    CAP = cap.add(seleção, CAP)
    
    
    while (CurrentTime <= Tfim) and (pop.dim(população)!=0): 
        #simulação para quando não houver mais indivíduos ou chegar ao fim do tempo
        
        #inicializar o próximo evento
        EventoAtual = cap.nextE(CAP) #evento atual é o próximo da CAP
        CAP = cap.delete(CAP) #elimina o evento atual da CAP
        CurrentTime = event.time(EventoAtual)
        check = pop.ident(população, event.ident(EventoAtual))
        if check != False: #se o evento atual for de um indivíduo que não existe, pop.ident devolve False
        
            if event.kind(EventoAtual) == "avaliação": #se o proximo evento for avaliação
                
                avaliado = pop.ident(população, event.ident(EventoAtual)) #define o indivíduo a ser avaliado
                A = ind.coef(avaliado) #calcula o coeficiente de adaptação do avaliado
                I = CurrentTime - ind.idade(avaliado) #calcula a idade do avaliado

                if random.random() < (1-(2/pi)*atan((1+A)**(1+8/(1+I)))): #probabilidade do avaliado morrer
                    população = pop.kill(população, avaliado) #retira o avaliado da população

                else: #se não morrer, marca-se a próxima avaliação
                    avaliação = event.event("avaliação", ind.ident(avaliado), CurrentTime + exprandom(Tlimiar))
                    CAP = cap.add(avaliação, CAP)

                    
            elif event.kind(EventoAtual) == "evolução": #se o próximo evento for uma evolução
                
                avaliado = pop.ident(população, event.ident(EventoAtual)) #individuo a ser avaliado
                T = pop.dim(população) #calcula a dimensão da população atual

                if random.random() < 1/(1+e**((K-T)/10)): #probabilidade de haver uma mutação
                    novo = copy.deepcopy(avaliado)
                    novo = ind.mutation(novo) #cria um indivíduo novo, que é a mutação do indivíduo avaliado
                    if ind.coef(novo) > ind.coef(avaliado): #substitui o avaliado pelo novo, se o novo for melhor
                        população = pop.kill(população, avaliado) #elimina o avaliado
                        população = pop.addI(população, novo) #adiciona o novo
                        #não é preciso atualizar eventos, porque o novo tem o mesmo identificador (na prática, é o mesmo indivíduo)

                else: #se não houver uma mutação, há uma reprodução
                    novo = copy.deepcopy(avaliado)
                    filho = ind.new(ind.colour(novo), CurrentTime, identificador) #cria o filho, com a mesma coloração
                    filho = ind.mutation(filho) #provoca uma mutação no filho
                    população = pop.addI(população, filho) #adiciona o filho à população
                    avaliação = event.event("avaliação", identificador, CurrentTime + exprandom(Tlimiar)) #próxima avaliação do filho
                    CAP = cap.add(avaliação, CAP)
                    evolução = event.event("evolução", identificador, CurrentTime + exprandom(Tritmo)) #próxima evolução do filho
                    CAP = cap.add(evolução, CAP)
                    identificador += 1

                evolução = event.event("evolução", ind.ident(avaliado), CurrentTime + exprandom(Tritmo)) #próxima evolução do avaliado
                CAP = cap.add(evolução, CAP)
                
                
            else: #se o próximo evento for uma seleção

                while ind.coef(pop.worst(população)) < 1 and (pop.dim(população)!=0): #elimina os indivíduos inválidos (com coeficientes <1)
                    população = pop.kill(população,pop.worst(população)) #elimina o pior indivíduo
                
                while pop.dim(população) > K*(3/2) and (pop.dim(população)!=0): #elimina os piores válidos, de forma a controlar o tamanho da população
                    população = pop.kill(população,pop.worst(população))  #elimina o pior indivíduo  
                    
                seleção = event.event("seleção", 0, CurrentTime + exprandom(Tfiltro)) #próximo evento de seleção
                CAP = cap.add(seleção, CAP)
    #fim do ciclo


    if pop.dim(população)==0: #se o ciclo parou porque não havia mais indivíduos
        return 'A simulação parou porque foram eliminados todos os indivíduos'
    
    else:
        vencedor = pop.best(população) #vê qual o melhor sobrevivente
        coloração = ind.colour(vencedor) #vê a coloração do melhor
        return color.show(coloração) #mostra a  melhor coloração
