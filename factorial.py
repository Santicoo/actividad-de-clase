def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input("Ingrese el número del cual desea saber el factorial: "))
print("Resultado:", factorial(n))