def frequenza2(dati):
    n = 0
    for i in dati:
        if n <= i :
            n = i+1
    
    lista = [0] * n
    
    for i in dati:
        lista[i] += 1

    return lista

def main():
    lista = [0, 0, 15, 15, 15, 2]
    print(lista)

    lista = frequenza2(lista)
    print(lista)

main()