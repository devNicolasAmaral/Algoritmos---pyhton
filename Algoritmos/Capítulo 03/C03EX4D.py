tempo = int(input("Apresente o tempo: "))
velocidade = int(input("Apresente a velocidade: "))
distancia = velocidade * tempo
litros_usados = distancia / 12
print("A velocidade média foi", velocidade, "Km/h")
print("O tempo gasto foi", tempo, "horas")
print("A distância média foi", distancia, "Km")
print("A quantidade de litros utilizados foi", litros_usados, "L")
