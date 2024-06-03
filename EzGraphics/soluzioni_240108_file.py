def esercizio1():
    prod = 1
    with open("prova.txt", "r") as f:
        for line in f:
            prod *= int(line)
    return prod

def esercizio2(filename = "prova.txt"):
    # È esattamente uguale al precedente, con l'unica differenza che il nome
    # del file nella chiamata ad `open` è il parametro `filename`.
    prod = 1
    with open(filename, "r") as f:
        for line in f:
            prod *= int(line)
    return prod

def esercizio3(filename):
    # inizializzo le variabili che contano linee, caratteri e parole
    count_lines = 0
    count_words = 0
    count_chars = 0
    with open(filename, "r") as f:
        for line in f:
            count_lines += 1
            count_chars += len(line)
            # Uso il metodo `split()` per dividere la stringa `line` in un
            # array di parole. La lunghezza di questo array è il numero di
            # parole in `line`.
            words = line.split()
            count_words += len(words)
    return count_lines, count_words, count_chars

def copyfile(src, dst):
    # Apro entrambi file (src in lettura e dst in scrittura). Leggo una riga
    # alla volta da src e la scrivo in dst.
    with open(src, "r") as fsrc, open(dst, "w") as fdst:
        for line in fsrc:
            fdst.write(line)

def file_exist(filename):
    # Inizializzo la variabile `found` a True: se non si verifica nessun
    # errore, questo sarà il valore che verrà restituito.
    found = True
    try:
        # Apro un file e non faccio nulla
        with open(filename, "r") as f:
            pass
    except FileNotFoundError:
        # Se si è verificato un errore, allora il file non esiste e
        # metto found a False.
        found = False
    return found

def esercizio6():
    # Dovrebbe essere un programma, ma lo scriviamo sotto forma di funzione in modo da
    # poter mettere tutto nello stesso file Python.
    while True:
        src = input("Immetti file sorgente: ")
        if file_exist(src):
            break
    dst = input("Immetti file detinazione: ")
    copyfile(src, dst)

print(esercizio3("prova2.txt"))