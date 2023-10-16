def newC(grafo):
    return [grafo,[]]


def fill(final):
    for x in range(graph.size(final[0])):
        final += []



def size(final):
    return graph.size(final[0])



def paint(final): #adicionar cores se quisermos identificar cores pelo nome
    i = 0
    while i < size(final[1]):
        final[i] = 0
        i += 1
    return final

def paintR(final, cores):
    i = 0
    while i < size(final[1]):
        final[i] = random(cores)
        i += 1
    return final

    