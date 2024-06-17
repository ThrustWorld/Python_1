
def frequenza(dati):
    lista = [0] * 10
    
    for i in dati:
        lista[i] += 1

    return lista

def main():
    lista = []
    with open("Exams/1/dati.txt", "r") as file:
        for linea in file:
            lista.append(int(linea))

    risultato = frequenza(lista)
    for i in range(10):
        print(i, "*" * risultato[i])

main()