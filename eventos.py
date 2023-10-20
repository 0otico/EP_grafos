#Um evento é uma lista e com 3 elementos: 
#e[0] é o tipo do evento; 
#e[1] é o identificador do indivíduo a quem o evento acontece; 
#e[2] é o instante em que acontece.

def event(k,i,t): #cria um evento do tipo k, a acontecer ao indivíduo i no instante t
    return [k,i,t]

def kind(e): #devolve o tipo do evento e
    return e[0]

def ident(e): #devolve o indivíduo a quem vai acontecer o evento e
    return e[1]

def time(e): #devolve o instante em que vai acontecer o evento e
    return e[2]