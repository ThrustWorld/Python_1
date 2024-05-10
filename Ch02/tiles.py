# Calcolare numero di piastrelle presenti in una riga dove la prima e l'ultima piastrella devono essere nere
tile_width = 5
row_width = 100
first_black_tile = 1

total_width = row_width - tile_width

tiles_for_row = total_width // (tile_width * 2)  # coppia di piastrelle: bianca-nera, / = parte intera + resto, // = parte intera, % = resto
print("pair of tiles:", tiles_for_row)

total_tiles = tiles_for_row * 2 + first_black_tile   # numero piastrelle totali + prima piastrella nera
print("total of tiles:", total_tiles)

edge_space = (row_width - (total_tiles * tile_width)) / 2 # spazio omogeneo alle due estremità
print("space between edges:", edge_space)