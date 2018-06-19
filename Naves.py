import random
def perderPaquetes(perdida):
    print('Probabilidad: ',perdida)
    viajes = 300
    meses = 12
    perdidasMensuales = [0]*meses
    sizePM = len(perdidasMensuales)
    for j in range(0,sizePM):
        totalPerdidos = 0
        consecutivos = 0
        auxiliar = 0
        for i in range(0,viajes):
            r = random.random()
            if(r < perdida):
                totalPerdidos = totalPerdidos + 1
                consecutivos = consecutivos + 1
            else:
                if(consecutivos > auxiliar):
                    auxiliar = consecutivos
                consecutivos = 0
            #if(i == viajes-1):
                #print('********************************')
                #print('Ultimo random: ',r)
                #print('Total perdidos: ',totalPerdidos)
                #print('Total consecutivos: ',auxiliar)
                #print('Total consecutivos: ',consecutivos)
                #print('********************************')
        perdidasMensuales[j] = auxiliar
    print('Promedio')
    acum = 0
    for i in range(0,meses):
        acum = acum + perdidasMensuales[i]
    print('Perdida anual: ',acum)    
    acum= acum / meses
    print('Perdida mensual estimada: ',acum)
    return acum
    #promedio(perdidasMensuales, meses)

def promedio(perdidas, meses):
    acum = 0
    for i in range(0,meses):
        acum = acum + perdidas[i]
    print('Perdida anual: ',acum)    
    acum = acum / meses
    print('Perdida mensual estimada: ',acum)    

def epsilon(epsi):
    #nave de tipo c
    perdida = 0.1
    #epsi = 0.25
    pAnterior = 0
    pActual = 0
    p = 0
    paquetesPerdidos = 0
    envios = 300
    bandera = True
    i = 1
    while(i < envios and bandera == True):
    #for i in range(0,envios):
        r = random.random()
        pAnterior = pActual
        if(r < perdida):
            paquetesPerdidos = paquetesPerdidos + 1
            pActual = paquetesPerdidos / i
            p = pAnterior - pActual
            if(p < epsi):
                bandera = False  
        i = i + 1
    print('Probabilidad: ',p)
    print('Envios hechos: ',i)
    print('Paquetes perdidos: ',paquetesPerdidos)        

def despedir():
    pA = 0.01
    pB = 0.05
    pC = 0.1
    cant = 40
    naves = [0]*cant
    #llamo a la funcion
    for i in range(0,10):
        # ciclo de las naves tipo A
        naves[i] = perderPaquetes(pA)
    
    for i in range(10,25):
        # ciclo de las naves tipo B
        naves[i] = perderPaquetes(pB)

    for i in range(25,40):
        # ciclo de las naves tipo C
        naves[i] = perderPaquetes(pC)
    # incompleta :(
    

