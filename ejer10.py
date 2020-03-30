n1 = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n1 % i != 0:
    i += 1
if i == n1:
    print(str(n1) + " es primo")
else:
    print(str(n1) + " no es primo")