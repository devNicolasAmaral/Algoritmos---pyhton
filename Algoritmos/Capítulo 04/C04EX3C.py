print("Média escolar")
print()
n1 = float(input("Entre a primeira nota: "))
n2 = float(input("Entre a segunda nota: "))
n3 = float(input("Entre a terceira nota: "))
n4 = float(input("Entre a quarta nota: "))
md = (n1 + n2 + n3 + n4) / 4
print()
if (md > 5):
    print("aprovado")
else:
    print("reprovado")
    