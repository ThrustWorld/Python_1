"""
Programma per giocare a Forza 4 tra due giocatori umani.

Lo stato attuale della griglia del gioco viene memorizzato in una matrice di interi.
Ogni cella della matrice corrisponde ad una posizione nella griglia del gioco. Il valore 0
indica che la cella è vuota. Un valore positivo indica la presenza di un gettone del
giocatore blu, mentre un valore negativo indica il gettone del giocatore rosso.
La dimensione del campo da gioco può variare da una partita all'altra.
"""

from ezgraphics import GraphicsWindow, GraphicsCanvas

CELL_SIZE = 40
LINE_WIDTH = 5

def show_board(board, canvas: GraphicsCanvas):
    """
    Visualizza la griglia di gioco.
    """
    # Notare che potrebbe essere più efficiente disegnare la griglia vuota all'inizio
    # del gioco, e poi aggiungere di volta il volta solo l'ultima mossa. Si è scelto la
    # strada di ridisegnare tutto dall'inizio perché è quello che vi consiglio per il
    # progetto d'esame, dato che in quel caso non è ovvio capire quali celle vanno
    # ridisegnate e quali no.
    canvas.clear()
    for y in  range(len(board)):
        for x in range(len(board[y])):
            x0 = x * CELL_SIZE
            y0 = y * CELL_SIZE
            canvas.setOutline("black")
            canvas.setFill()
            canvas.setLineWidth(1)
            canvas.drawRect(x0, y0, CELL_SIZE, CELL_SIZE)
            if board[y][x] > 0:
                canvas.setColor("blue")
                canvas.setLineWidth(LINE_WIDTH)
                canvas.drawOval(x0+LINE_WIDTH, y0+LINE_WIDTH, CELL_SIZE-2*LINE_WIDTH, CELL_SIZE-2*LINE_WIDTH)
            elif board[y][x] < 0:
                canvas.setColor("red")
                canvas.setLineWidth(LINE_WIDTH)
                canvas.drawOval(x0+LINE_WIDTH, y0+LINE_WIDTH, CELL_SIZE-2*LINE_WIDTH, CELL_SIZE-2*LINE_WIDTH)

def show_winner(winner, canvas: GraphicsCanvas):
    """
    Visualizza il vincitore della partita.
    """
    width = canvas.width()
    height = canvas.height()
    canvas.setOutline("black")
    canvas.setFill("white")
    canvas.drawRectangle(0, height // 3, width, height // 3)
    canvas.setFontSize(20)
    canvas.setTextAnchor("center")
    text = "Vince giocatore blu" if winner > 0 else "Vince giocatore rosso" if winner < 0 else "Pari"
    canvas.drawText(width // 2, height // 2, text)

def create_empty_board(num_rows, num_cols):
    """
    Crea un matrice rappresentante la griglia di gioco con "num_rows" righe e "num_cols" colonne,
    completamente vuota (ovvero tutti gli elementi della matrice contengono 0).
    """
    # Funzione vista più e più volte. Consultare ad esempio il notebook della lezione
    # del 7 dicembre.
    board = []
    for i in range(num_rows):
        board.append([0] * num_cols)
    return board

def check_move(board, col):
    """
    Controlla che, data la griglia di gioco rappresentana dalla lista "board", la mossa di mettere
    un gettone nella colonna "col" sia valida. Più precisamente, la mossa è valida se "col" è
    compreso tra 0 e il numero di colonne massimo possibile, e se nella colonna "col" c'è spazio
    per inserire un nuovo gettone.
    """
    # È sufficiente controllare se la prima riga della colonna "col" è vuota. Se lo
    # è, vuol dire che nella colonna "col" possiamo mettere un gettone, altrimenti
    # vuol dire che la colonna è piena.
    return 0 <= col < len(board[0]) and board[0][col] == 0

def move(board, col, player):
    """
    Modifica l'array "board", con il nuovo stato del gioco che consegue all'inserimento di un
    gettone del giocatore "player" nella colonna "col". Notare che questo metodo viene chiamato
    solo se la mossa di inserire un gettone nella colonna "col" è valida, quindi si può ignorare
    il caso che la mossa non sia valida.
    """
    # Scandisce la colonna "col" di board (dalla prima all'ultima riga, ovvero dall'alto
    # verso il basso nella prospettiva di Forza 4) alla ricerca della prima posizione occupata.
    i = 0
    while i < len(board) and board[i][col] == 0:
        i += 1
    # Se i è la prima riga occupata, allora i-1 è l'ultima libera.
    board[i-1][col] = player

def winner_from(board, r, c):
    """
    Considera la cella in riga "r" e colonna "c" della griglia rappresentata in "board". Se da
    quella cella parte una sequenza di gettoni che rende vincente il giocatore g, allora
    restituisce g. In caso contrario, restituisce uno 0.
    """
    player = board[r][c]
    if (c <= len(board[0]) - 4
        and board[r][c + 1] == player
        and board[r][c + 2] == player
        and board[r][c + 3] == player):
            return player
    if (r <= len(board) - 4
        and board[r + 1][c] == player
        and board[r + 2][c] == player
        and board[r + 3][c] == player):
            return player
    if (r <= len(board) - 4
        and c <= len(board[0]) - 4
        and board[r + 1][c + 1] == player
        and board[r + 2][c + 2] == player
        and board[r + 3][c + 3] == player):
            return player
    if (r <= len(board) - 4
        and c >= 3
        and board[r + 1][c - 1] == player
        and board[r + 2][c - 2] == player
        and board[r + 3][c - 3] == player):
            return player
    return 0

def winner(board):
    """
    Restituisce il giocatore vincitore in una determinata configurazione di gioco, 0 se non vince nessuno.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            winner = winner_from(board, i, j)
            if winner != 0:
                return winner
    return 0

def get_move(win: GraphicsWindow):
    """
    Restituisce la mossa del giocatore: aspetta un click del mouse e calcola la colonna
    in cui è avvenuta.
    """
    x, y = win.getMouse()
    return x // CELL_SIZE

def main(num_rows, num_cols):
    """
    Programma principale del gioco di Forza 4.
    """
    win = GraphicsWindow(num_rows*CELL_SIZE, num_cols*CELL_SIZE)
    win.setTitle("Forza 4")
    canvas = win.canvas()
    board = create_empty_board(num_rows, num_cols)
    # giocatore corrente
    player = 1
    # numero mosse effettuate
    moves = 0
    while winner(board) == 0 and moves < num_rows * num_cols:
        # visualizza la tavola da gioco
        show_board(board, canvas)
        # prende la mossa del giocatore
        col = get_move(win)
        # controlla se la mossa è valid
        if check_move(board, col):
            # se è valida la esegue, poi incrementa la variabile moves e
            # cambia il giocatore corrente
            move(board, col, player)
            moves += 1
            player *= -1
    show_board(board, canvas)
    show_winner(winner(board), canvas)
    win.getMouse()


if __name__ == "__main__":
    main(10, 10)