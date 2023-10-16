def newC():
    return []


def fill(final,N):
    for x in range(N):
        final += []



def size(final):
    for x in final:
        i += 1
    return i



def paint(final): #adicionar cores se quisermos identificar cores pelo nome
    i = 0
    while i < size(final):
        final[i] = 0
        i += 1
    return final

def paintR(final, cores):
    i = 0
    while i < size(final):
        final[i] = random(cores)
        i += 1
    return final

    