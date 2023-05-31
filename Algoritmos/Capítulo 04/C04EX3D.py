print("Média escolar")
print()
n1 = float(input("Entre a primeira nota: "))
n2 = float(input("Entre a segunda nota: "))
n3 = float(input("Entre a terceira nota: "))
n4 = float(input("Entre a quarta nota: "))
md1 = (n1 + n2 + n3 + n4) / 4
print()
if (md1 > 7):
    print("aprovado")
    print("A média é", "%.2f" % md1)
else:
    ne = float(input("Entre a nota de exame: "))
    md2 = (ne + md1) / 2
    if (md2 > 5 ):
        print("Aprovado em exame")
        print("A média é", "%.2f" % md2)
    else:
        print("Reprovado")
        print("A média é", "%.2f" % md2)
