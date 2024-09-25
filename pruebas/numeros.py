def BuscaMultiplos(numero, limite):
    for i in range(numero,limite + 1):
        if i % numero == 0: 
            print (i) 
            

BuscaMultiplos(2,10)