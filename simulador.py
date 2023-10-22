#módulos
import grafos as graph 
import colorações as color 
import indivíduos as ind 
import população as pop 
import eventos as event 
import CAP as cap 

#para fazer contas de probabilidade
import random as random #extensão com random, randrange
from math import pi 
from math import log 
from math import e

def exprandom(m):
    x=random()
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
    if (type(Tfiltro)!=float and type(Tfiltro)!=int) or Tflitro<=0:
        return 'Erro: a variável Tfiltro tem de ser um número positivo'

    #inicalizar as variáveis
    CurrentTime = 0 #o instante em que estamos
    identificador = 1 #identificador do próximo indivíduo a ser criado
    população = pop.new() #cria a lista de individuos
    cap = cap.new() #cria a lista de eventos

    #inicializar a população e a CAP
    cores = [x+1 for x in range(graph.dim(G))] #coloração da população inicial
    for k in range(K):
        indivíduo = ind.new(cores, CurrentTime, identificador) #cria o indivíduo novo 
        população = pop.addI(população, indivíduo) #junta o indivíduo novo à população
        avaliação = event.event("avaliação", identificador, CurrentTime + exprandom(Tlimiar)) #próxima avaliação do novo indivíduo
        cap = cap.add(avaliação, cap) #adiciona a avaliação à CAP
        evolução = event.event("evolução", identificador, CurrentTime + exprandom(Tritmo)) #próxima evolução do novo indivíduo
        cap = cap.add(evolução, cap) #adiciona a evolução à CAP
        identificador += 1
        
    #próximo evento de seleção global
    seleção = event.event("seleção", 0, CurrentTime+exprandom(Tfiltro)) #0 serve como default, porque a seleção afeta todos
    cap = cap.add(seleção, cap)
    
    
    while CurrentTime <= Tfinal and pop.dim(população)!=0: 
        #simulação para quando não houver mais indivíduos ou chegar ao fim do tempo
        
        #inicializar o próximo evento
        EventoAtual = pop.nextE(cap) #evento atual é o próximo da CAP
        cap = pop.delete(cap) #elimina o evento atual da CAP
        CurrentTime = event.time(EventoAtual)
        
        
        if event.kind(EventoAtual) == "avaliação": #se o proximo evento for avaliação
            
            avaliado = pop.ident(população, event.ident(EventoAtual)) #define o indivíduo a ser avaliado
            A = ind.coef(avaliado) #calcula o coeficiente de adaptação do avaliado
            I = CurrentTime - ind.idade(avaliado) #calcula a idade do avaliado

            if random() < (1-(2/pi)*arctan((1+A)**(1+8/(1+I)))): #probabilidade do avaliado morrer
                população = pop.kill(população, avaliado) #retira o avaliado da população
                cap = cap.delete_id(cap, avaliado) #elimia todos os eventos respeitantes ao avaliado

            else: #se não morrer, marca-se a próxima avaliação
                avaliação = event.event("avaliação", avaliado, CurrentTime + exprandom(Tlimiar))
                cap = cap.add(avaliação, cap)

                
        elif event.kind(EventoAtual) == "evolução": #se o próximo evento for uma evolução
        
            avaliado = pop.ident(população, event.ident(EventoAtual)) #individuo a ser avaliado
            T = pop.dim(população) #calcula a dimensão da população atual

            if random() < 1/(1+e**((K-T)/10)): #probabilidade de haver uma mutação
                novo = ind.mutation(avaliado) #cria um indivíduo novo, que é a mutação do indivíduo avaliado
                if ind.coef(novo) > ind.coef(avaliado): #substitui o avaliado pelo novo, se o novo for melhor
                    população = pop.kill(população, avaliado) #elimina o avaliado
                    população = pop.addI(população, novo) #adiciona o novo
                    #não é preciso atualizar eventos, porque o novo tem o mesmo identificador (na prática, é o mesmo indivíduo)

            else: #se não houver uma mutação, há uma reprodução
                filho = ind.new(ind.color(avaliado), CurrentTime, identificador) #cria o filho, com a mesma coloração
                filho = ind.mutation(filho) #provoca uma mutação no filho
                população = pop.addI(população, filho) #adiciona o filho à população
                avaliação = event.event("avaliação", identificador, CurrentTime + exprandom(Tlimiar)) #próxima avaliação do filho
                cap = cap.add(avaliação, cap)
                evolução = event.event("evolução", identificador, CurrentTime + exprandom(Tritmo)) #próxima evolução do filho
                cap = cap.add(evolução, cap)
                identificador += 1

            evolução = event.event("evolução", ind.ident(avaliado), CurrentTime + exprandom(Tritmo)) #próxima evolução do avaliado
            cap = cap.add(evolução, cap)
            
            
        else: #se o próximo evento for uma seleção
            
            while ind.coef(pop.worst(população)) < 1: #elimina os indivíduos inválidos (com coeficientes <1)
                população = pop.kill(pop.worst(população)) #elimina o pior indivíduo
                cap = cap.delete_id(cap, popu.worst(população)) #elimina os eventos do indivíduo eliminado
               
            while pop.dim(população) > K*(3/2): #elimina os piores válidos, de forma a controlar o tamanho da população
                população = pop.kill(pop.worst(população)) #elimina o pior indivíduo
                cap = cap.delete_id(cap, popu.worst(população)) #elimina os eventos do indivíduo eliminado

            seleção = event.event("seleção", 0, CurrentTime + exprandom(Tfiltro)) #próximo evento de seleção
            cap = cap.add(seleção, cap)
    #fim do ciclo


    if pop.dim(população)==0: #se o ciclo parou porque não havia mais indivíduos
        return 'A simulação parou porque foram eliminados todos os indivíduos'
    
    else:
        vencedor = pop.best(população) #vê qual o melhor sobrevivente
        coloração = ind.color(vencedor) #vê a coloração do melhor
        return color.show(coloração) #mostra a  melhor coloração
