def main():
    values = [9, 13, 21, 4, 11, 7, 1, 3]
    i = 0 # prima metà della lista
    j = len(values) // 2 # seconda metà della lista
    while i < len(values) // 2 :
        swap(values, i, j) # inversione delle posizioni dei valori
        i = i + 1
        j = j + 1
    print(values)

def swap(a, i, j): 
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

main()