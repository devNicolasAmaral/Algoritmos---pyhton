print("Eleição sindical")
print()
a = int(input("Votos para o candidato A: "))
b = int(input("Votos para o candidato B: "))
c = int(input("Votos para o candidato C: "))
nulo = int(input("Votos nulos: "))
branco = int(input("Votos em branco: "))
print()
totalEleitores = a + b + c + nulo + branco
totalEleitoresA = a * 100 / totalEleitores
totalEleitoresB = b * 100 / totalEleitores
totalEleitoresC = c * 100 / totalEleitores
totalNulo = nulo * 100 / totalEleitores
totalBranco = branco * 100 / totalEleitores
print("O total de eleitores é " + str(totalEleitores))
print("Porcentagem de votos validos para o candidato A: " + str("%.2f" % totalEleitoresA) + "%")
print("Porcentagem de votos validos para o candidato B: " + str("%.2f" % totalEleitoresB) + "%")
print("Porcentagem de votos validos para o candidato C: " + str("%.2f" % totalEleitoresC) + "%")
print("Porcentagem de votos nulos: " + str("%.2f" % totalNulo) + "%")
print("Porcentagem de votos brancos: " + str("%.2f" % totalBranco) + "%")
