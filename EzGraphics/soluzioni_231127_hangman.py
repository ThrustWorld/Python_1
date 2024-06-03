from ezgraphics import GraphicsWindow, GraphicsCanvas
from random import choice

# numero massimo di errori ammissibili
MAX_ERRORS = 5

def display_hangman(canvas: GraphicsCanvas, n, word):
    """
    Visualizza nel `canvas` la figura dell'impiccato. La variabile `n` contiene il numero
    di errori commessi, che determina quali parti della figura vanno disegnate. In aggiunta,
    sotto la figura dell'impiccato la funzione deve visualizzare la parola che si sta
    cercando di individuare, che trovato nel parametro `word`.
    """
    canvas.drawLine(0,300,399,300)
    canvas.drawLine(100, 300, 100, 20)
    canvas.drawLine(100, 20, 200,20)
    canvas.drawLine(200,20, 200, 50)
    if n > 0:
        # testa
        canvas.drawOval(175, 50, 50, 50)
    if n > 1:
        # corpo
        canvas.drawLine(200,100, 200, 200)
    if n > 2:
        # braccio sx
        canvas.drawLine(200, 110, 150, 150)
    if n > 3:
        # braccio dx
        canvas.drawLine(200, 110, 250, 150)
    if n > 4:
        # gamba sx
        canvas.drawLine(200, 200, 150, 240)
    if n > 5:
        # gamba dx
        canvas.drawLine(200, 200, 250, 240)
    # Il metodo setTextAnchor fa in modo che, nella successiva chiamata a
    # drawText, le coordinate indicate siano quelle del centro della stringa
    # e non quelle a sinistra.
    canvas.setTextAnchor("center")
    canvas.setFontSize(20)
    canvas.drawText(200, 350, word)

def hide_word(word, found_letters):
    """
    Restituisce una nuova stringa ottenuta ricopiando `word` ma in modo tale che
    le lettere che NON SONO PRESENTI nella lista `letters` siano rimpiazzate con
    un segno meno.
    """
    result = ""
    for c in word:
        if c in found_letters:
            # non possiamo usare append per aggiungere i caratteri a result
            # perché append non è un metodo valido per le stringhe ma solo per le
            # liste (almeno tra i tipi che conosciamo noi)
            result += c
        else:
            result += "-"
    return result

def choose_word():
    """
    Restituisce una parola casuale.
    """
    # Usiamo una tupla, ma potremmo utilizzare anche una lista
    parole = "cane", "gatto", "coccodrillo", "zuzzurellone", "ippopotamo"
    # La funzione choice del modulo random restituisce un elemento a caso di una
    # lista, in alternativa è possibile ottenere lo stesso effetto dell'ultima riga
    # con le righe:
    # i = randint(0, len(parole)-1)
    # return parole[i]
    return choice(parole)

def found_word(word, letters):
    """
    Restuisce True se la stringa `word` è costituita interamente da lettere in `letters`,
    False altrimenti.
    """
    for c in word:
        if c not in letters:
            return False
    return True

def count_errors(word, letters):
    """
    Restituisce il numero di lettere in `letters` che non compaiono in `word`.
    """
    num_errors = 0
    for l in letters:
        if l not in word:
            num_errors += 1
    return num_errors

def display_lost_match(canvas):
    """
    Visualizza un segno per indicare che il gioco è stato perso.
    """
    canvas.setColor("red")
    canvas.setLineWidth(5)
    canvas.drawLine(150,20,250,240)
    canvas.drawLine(250,20,150,240)

def display_won_match(canvas):
    """
    Visualizza un segno per indicare che il gioco è stato vinto.
    """
    canvas.setColor("green")
    canvas.setLineWidth(5)
    canvas.drawLine(175,175,200,200)
    canvas.drawLine(200,200,300,100)

def main():
    win = GraphicsWindow()
    win.setTitle("Hangman")
    canvas = win.canvas()
    # la variabile word contiene la parola da cercare
    word = choose_word()
    # la variabile tried_lettes conterrà l'elenco delle lettere provate dal giocatore
    tried_letters = []
    while True:
        canvas.clear()
        # determina la parola con le lettere nascoste
        hidden_word = hide_word(word, tried_letters)
        # determina il numero di errori commessi
        num_errors = count_errors(word, tried_letters)
        display_hangman(canvas, num_errors, hidden_word)
        # se ho commesso troppi errori o ho trovato la parola, esci dal gioco
        if num_errors > MAX_ERRORS or found_word(word, tried_letters):
            break
        key = win.getKey()
        # se la lettera non è mai stata provata prima
        if not key in tried_letters:
            # aggiungi all'elenco delle lettere provate
            tried_letters.append(key)
    if num_errors > MAX_ERRORS:
        display_lost_match(canvas)
    else:
        display_won_match(canvas)
    win.getKey()

if __name__ == "__main__":
    main()
