# Risposta: ritorna ac [4 call di mistero(l, n, r)]

def mistero(l, n, r):
    if n == len(l):
        return r
    elif n % 2 == 0:
        return mistero(l, n+1, l[n] + r)
    else:
        return mistero(l, n+1, r)



x = mistero("ciao", 0, "")
print(x)