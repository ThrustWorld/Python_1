def main():
    area = triangle_area(10)
    print("Area:", area)
    print("Expected:", 55)

def triangle_area(side_length):
    if side_length <= 0 : # caso speciale che termina la ricorsione
        return 0
    if side_length == 1 : # caso speciale che termina la ricorsione
        return 1
    smaller_side_length = side_length - 1 # riduzione complessità del problema
    smaller_area = triangle_area(smaller_side_length) # ricorsione
    area = smaller_area + side_length
    return area # Esecuzione alla fine del processo totale di ricorsione

main()