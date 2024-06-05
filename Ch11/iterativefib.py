def main():
    n = int(input("Enter n: "))
    for i in range(1, n + 1):
        f = fib(i)
        print("fib((%d) = %d" % (i, f))


def fib(n): # velocità di esecuzione poichè la funzione viene invocata una sola volta
    if n <= 2 :
        return 1
    else:
        first_value = 1
        second_value = 1
        new_value = 1
        for i in range(3, n + 1):
            new_value = first_value + second_value
            first_value = second_value
            second_value = new_value
        return new_value
main()