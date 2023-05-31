print("Conversão de R$ em US$")
cotação = float(input("Apresente o valor da cotação do dólar: "))
real = float(input("Apresente o valor em real que deseja ser convertido para dólar: "))
dolar = real / cotação
print("R$" + str(real) + " equivale a US$" + str(dolar))
