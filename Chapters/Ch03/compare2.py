x = float(input("Number A: "))
y = float(input("Number B: "))


if x == y :
    print("A e B sono uguali")
else :
    if x > y :
        print("A è maggiore")
    else :
        print("B è maggiore")
    
    if -0.01 < x - y and x - y > 0.01 :
        print("A e B sono vicini")

    if x == y + 1 or x == y - 1 :
        print("A e B sono affiancati")

    if x > 0 and y > 0 or x < 0 and y < 0 :
        print("A e B hanno lo stesso segno")
    else :
        print("A e B hanno diverso segno") 