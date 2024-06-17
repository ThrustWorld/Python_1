def main():
    n = int(input("Enter n: "))
    for i in range(1, n + 1):
        f = fib(i)
        print("fib((%d) = %d" % (i, f))


def fib(n): # lentezza nei calcoli poichè la funzione viene invocata più volte
    if n <= 2 :
        return 1
    else:
        return fib(n - 1) + fib(n - 2) 


main()