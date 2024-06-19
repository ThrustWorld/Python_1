def somma_opposti(lista):
    if lista == [] : return True
    
    somma = lista[0] + lista[-1]

    for i in range(len(lista)):
       if lista[i] + lista[-1-i] != somma :
           return False
       
    return True

risultato = somma_opposti([1,1,1])

print(risultato)