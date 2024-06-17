def frequenza(dati):
    lista = [0] * 10
    
    for i in dati:
        lista[i] += 1

    return lista

def main():
    lista = [1, 2, 3, 1, 9, 9, 7, 1]
    print(lista)

    lista = frequenza(lista)
    print(lista)

main()