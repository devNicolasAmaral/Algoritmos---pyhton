print("Velocidade de um projétil")
print()
distância = float(input("Apresente a distância percorrida: "))
tempo = float(input("Apresente o tempo gasto: "))
velocidade = (distância * 1000) / (tempo * 60)
print("A velocidade é igual à " + str("%.2f" % velocidade) + " m/s")

