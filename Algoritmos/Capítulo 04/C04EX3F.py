print("Ordem Crescente")
print()
a = int(input("Entre o primeiro valor: "))
b = int(input("Entre o segundo valor: "))
c = int(input("Entre o terceiro valor: "))
if (a > b):
    x = a
    a = b
    b = x
if (a > c):
    x = a
    a = c
    c = x
if (b > c):
    x = b
    b = c
    c = x
print(a, b, c)


