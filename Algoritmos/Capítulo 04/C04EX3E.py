print("Cálculo de uma operação de segundo grau")
print()
a = int(input("Entre o primeiro valor: "))
b = int(input("Entre o segundo valor: "))
c = int(input("Entre o terceiro valor: "))
delta = b ** 2 - 4 * a * c
x1 = (-b + delta ** 1/2) / 2 * a
x2 = (-b - delta ** 1/2) / 2 * a
if (delta > 0):
    print("O valor de x1 é", x1)
    print("O valor de x2 é", x2)
elif (delta == 0):
    print("O valor de x é", x1)
elif (delta < 0):
    print("Não há solução real")