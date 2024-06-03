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

def show_board(board):
    """
    Visualizza la griglia di gioco sul terminale.
    """
    for riga in board:
        print("|", end="")
        for gettone in riga:
            ch = "X" if gettone > 0 else "O" if gettone < 0 else " "
            print(ch, end="")
            print("|", end="")
        print()


def show_winner(winner):
    """
    Visualizza il vincitore della partita.
    """
    text = "Vince giocatore X" if winner > 0 else "Vince giocatore O" if winner < 0 else "Pari"
    print(text)

def create_empty_board(num_rows, num_cols):
    """
    Crea un lista rappresentante la griglia di gioco con "num_rows" righe e "num_cols" colonne,
    completamente vuota (ovvero tutti gli elementi della matrice contengono 0).
    """
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
    return col >= 0 and col < len(board[0]) and board[0][col] == 0

def move(board, col, player):
    """
    Modifica l'array "board", con il nuovo stato del gioco che consegue all'inserimento di un
    gettone del giocatore "player" nella colonna "col". Notare che questo metodo viene chiamato
    solo se la mossa di inserire un gettone nella colonna "col" è valida, quindi si può ignorare
    il caso che la mossa non sia valida.
    """
    i = 0
    while i < len(board) and board[i][col] == 0:
        i += 1
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

def get_move():
    """
    Restituisce la mossa del giocatore: aspetta un click del mouse e calcola la colonna
    in cui è avvenuta.
    """
    return int(input("Immetti mossa: "))

def main(num_rows, num_cols):
    """
    Programma principale del gioco di Forza 4.
    """
    board = create_empty_board(num_rows, num_cols)
    player = 1
    moves = 0
    while winner(board) == 0 and moves < num_rows * num_cols:
        show_board(board)
        col = get_move()
        if check_move(board, col):
            move(board, col, player)
            moves += 1
            player *= -1
    show_board(board)
    show_winner(winner(board))

if __name__ == "__main__":
    main(7, 6)