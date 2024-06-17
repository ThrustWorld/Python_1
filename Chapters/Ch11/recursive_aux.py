def palindroma_ricorsiva_aux(s, first, last):
    is_palindrome = None
    if last <= first:
        is_palindrome = True
        print(is_palindrome)         
        return is_palindrome
    elif s[first] != s[last]:
        is_palindrome = False
        print(is_palindrome)         
        return is_palindrome
    else:
        return palindroma_ricorsiva_aux(s, first+1, last-1)
    
def palindroma_ricorsiva(s):
    return palindroma_ricorsiva_aux(s, 0, len(s) - 1) # L'uso di una funzione ricorsiva ausiliaria permette di limitare gli argomenti di funzione 
                                      # solo a quelli essenzia

palindroma_ricorsiva("osso")
palindroma_ricorsiva("oblo")