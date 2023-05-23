numbers = int(input("Entrez la quantité de nombre à afficher : "))

a = 0
b = 1
total = 0

print("Les {0} premiers nombres de la suite de Fibonacci sont :".format(numbers), end = " ")
for _ in range(numbers):
    print(total, end = " ")
    a = b
    b = total
    total = a + b